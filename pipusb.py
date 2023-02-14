# Python v3.9.2 more information and dependencies, read requirements.txt
#0 Syntax camelCase

# Imports
import argparse
from time import sleep
import sys
import os
from notifypy import Notify
from usb import busses
from psutil import sensors_battery
from pydub import AudioSegment
from pydub.playback import play

#Path search
def path(relativePath):
  try:
    bacePath = sys._MEIPASS
  except Exception:
    bacePath = os.path.abspath(".")
  return os.path.join(bacePath, relativePath)

def list_devices():
  list_busses = busses()
  num_dev = int()
  for bus in list_busses:
    devices = bus.devices
    num_dev = len(devices) + num_dev

  return num_dev

def notification(text, noti, sound="", icon="", msg=""):
  if noti:
    notification = Notify(default_application_name="pipusb")
    notification.title = text
    if sound != "":
      notification.audio = path(sound)
    notification.icon = path(icon)
    notification.message = msg
    notification.send()
  else:
    song = AudioSegment.from_wav(path(sound))
    play(song)

# Main function
def main():

# Defining name, use and definition
  parser = argparse.ArgumentParser(prog = 'pipusb', formatter_class = argparse.RawDescriptionHelpFormatter, description = "Pipusb is a console program (CLI), which notifies with a customizable sound the insertion or removal of a USB device. Pipusb is designed to be as light and efficient as possible.\nDeveloped by @VidalGB")

# Version argument
  parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0', help = "show program's version number and exit.")

# Input sound
  parser.add_argument("-i","--input", type = str, default = './default/default_sound.wav', help = "file to play when inserting USB. (only .wav files are supported)")

# Output sound
  parser.add_argument("-o", "--output", type = str, default = './default/default_sound.wav', help = "file to play when removing USB. (only .wav files are supported)")

# dee
  parser.add_argument("-c", "--charger", action = 'store_true', help = 'detect charger.')

# ede
  parser.add_argument("-n", "--notification", action = 'store_true', help = 'show notification on USB detection.')
  args = parser.parse_args()
  
  old_devices = list_devices()
  flag_battery = True

  list_input = args.input.split('.')
  list_output = args.output.split('.')
  
  if list_input[-1] != "wav" or list_output[-1] != "wav":
    if args.notification:
      notification('file not supported, ".wav" files only', args.notification)
    else:
      sys.stdout.write('file not supported, ".wav" files only\n')
    sys.exit()
    
  try:
    while True:
      sleep(0.1)
      new_devices = list_devices()

      if new_devices > old_devices:
        notification("USB Connected", args.notification, args.input, './default/default_USB.png')

      if new_devices < old_devices:
        notification("USB Disconnected", args.notification, args.output, './default/default_USB.png')

      if args.charger:
        battery = sensors_battery()
        power = battery.power_plugged
        
        if power and flag_battery:
          flag_battery = False
          notification("Charger Connected", args.notification, args.input, './default/default_charger.png')

        if not power and not flag_battery:
          flag_battery = True

      old_devices = new_devices
      
  except KeyboardInterrupt:
    if args.notification:
      notification("pipusb was canceled by user", args.notification)
    else:
      sys.stdout.write('\npipusb was canceled by user\n')
    sys.exit()

  except Exception as e:
    if args.notification:
      notification('An unexpected error has occurred, please notify the developer.', args.notification, msg=f'Error > {e}')
    else:
      sys.stdout.write(f'An unexpected error has occurred, please notify the developer.\nError > {e}\n')
    sys.exit()


# Check script main
if __name__ == '__main__':
  main()
