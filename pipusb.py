# Python v3.9.2 more information and dependencies, read requirements.txt
# Syntax camelCase

# Imports
import argparse
import sys

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

# Check script main
if __name__ == '__main__':
  main()
