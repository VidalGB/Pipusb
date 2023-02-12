# Python v3.9.2 more information and dependencies, read requirements.txt
# Syntax camelCase

# Imports
import argparse
import usb
from playsound import playsound
import psutil
import time
from notifypy import Notify

def list_devices():
  busses = usb.busses()
  num_dev = int()
  for bus in busses:
    devices = bus.devices
    num_dev = len(devices) + num_dev

  return num_dev

def play_sound(sound):
  playsound(sound)

def notification(text, sound):
  notification = Notify(default_application_name="pipusb")
  notification.title = text
  notification.audio = sound
  notification.send()

# Main function
def main():

# Defining name, use and definition
  parser = argparse.ArgumentParser(prog = 'pipusb', formatter_class = argparse.RawDescriptionHelpFormatter, description = "PIPUSB")

# Version argument
  parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0', help = "show program's version number and exit.")

# Input sound
  parser.add_argument("-i","--input", type = str, default = './default/input_sound.mp3', help = "file to play when inserting USB. (only .wav files are supported)")

# Output sound
  parser.add_argument("-o", "--output", type = str, default = './default/input_sound.mp3', help = "file to play when removing USB. (only .wav files are supported)")

# dee
  parser.add_argument("-c", "--charger", action = 'store_true', help = 'detect charger.')

# ede
  parser.add_argument("-n", "--notification", action = 'store_true', help = 'show notification on USB detection.')
  args = parser.parse_args()
  
  old_devices = list_devices()
  while True:
    time.sleep(0.01)
    new_devices = list_devices()
    if new_devices > old_devices:
      if args.notification:
        notification("USB Connected", args.input)
      else:
        play_sound(args.input)

    if new_devices < old_devices:
      if args.notification:
        notification("USB Disconnected", args.output)
      else:
        play_sound(args.output)

    if args.charger:
      battery = psutil.sensors_battery()
      power = battery.power_plugged
      if power:
        play_sound(args.input)
    old_devices = new_devices

# Check script main
if __name__ == '__main__':
  main()
