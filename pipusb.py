# Python v3.9.2 more information and dependencies, read requirements.txt
# Syntax camelCase

# Imports
import argparse
import sys
import usb
from playsound import playsound
import psutil
import time

def ensambler_id(*args):
  parts = list()
  for part in args:
    part = part.split('x')
    part = part[1]
    len_part = len(part)
    if len_part < 4:
      more = 4 - len_part
      part = '0'*more + part
    parts.append(part)

  return f"{parts[0]}:{parts[1]}"

def list_devices():
  busses = usb.busses()
  num_dev = int()
  id_dev = dict()
  for bus in busses:
    devices = bus.devices
    for num, dev in enumerate(devices):
      id_vendor = "%s"%(hex(dev.idVendor))
      id_product = "%s"%(hex(dev.idProduct))
      id_dev[num + num_dev + 1] = ensambler_id(id_vendor, id_product)
    num_dev = len(devices) + num_dev

  return num_dev, id_dev

def play_sound(sound):
  playsound(sound)

# Main function
def main():

# Defining name, use and definition
  parser = argparse.ArgumentParser(prog = 'pipusb', formatter_class = argparse.RawDescriptionHelpFormatter, description = "PIPUSB")

# Version argument
  parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0', help = "show program's version number and exit.")

# Input sound
  parser.add_argument("-i","--input", type = str, default = './default/input_sound.mp3', help = "file to play of the input USB.")

# Output sound
  parser.add_argument("-o", "--output", type = str, default = './default/input_sound.mp3', help = "file to play of the output USB.")

# DeepL translator argument (free)
  parser.add_argument("-e", "--energize", action = 'store_true', help = 'energize.')
  args = parser.parse_args()
  
  old_devices = list_devices()
  while True:
    time.sleep(0.01)
    new_devices = list_devices()
    print(new_devices[0], old_devices[0])
    if new_devices[0] > old_devices[0]:
      play_sound(args.input)
    if new_devices[0] < old_devices[0]:
      play_sound(args.output)
    if args.energize:
      battery = psutil.sensors_battery()
      power = battery.power_plugged
      if power:
        play_sound(args.input)
    old_devices = new_devices


# Check script main
if __name__ == '__main__':
  main()
