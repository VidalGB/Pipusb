# Pipusb

Pipusb is a *lightweight and easy-to-use* terminal program for Linux that monitors USBs on the device and alerts you to changes in their status with a sound or a notification.

## Installation 

Download pipusb on [releases](https://github.com/VidalGB/Pipusb/releases)

Then open the terminal with `Ctrol` + `Alt` + `T` and go to the download section:

`cd ~/Downloads/`

After unzip the file 'pipusb_.x.tar.gz' with:

`tar –xvzf pipusb_.x.tar.gz`

Once extracted, navigate to the folder generated with:

`cd pipusb_.x`

Finally copy the pipusb file to '/bin/bash' to make it accessible to the whole system.

`sudo cp ./pipusb /usr/local/bin` or anywhere else in $PATH

### Compile

if you want to compile it yourself. **you need to have python >= 3.9.2 installed**

open the terminal with `Ctrol` + `Alt` + `T` and copy the repository with:

`git clone https://github.com/VidalGB/Pipusb.git`

Then move the generated folder with:

`cd ./Pipusb`

Now install the *Pyinstaler* module with the command:

`pip3 install pyinstaller` you may need to use 'sudo'

Compile the program with the following line

`pyinstaller build.spec`

and it will open compiled in the 'dist' folder the executable that you can place in the whole system by copying it with:

`sudo cp ./pipusb /usr/local/bin` or anywhere else in $PATH

# Usage

`pipusb [options]`

**Options:**

+ `-h` or `--help` > show help message and exit.
+ `-v` or `--version` > show program's version number and exit.
+ `-i [File.wav]` or `--input [File.wav]` > file to play when inserting USB. (only .wav files are supported)
+ `-o [File.wav]` or `--output [File.wav]` > file to play when removing USB. (only .wav files are supported)
+ `-c` or `--charger` > detect charger.
+ `-n` or `--notification` > show notification on USB detection.

# About us

Pipusb was developed by **@VidalGB**

-> [Github](https://github.com/VidalGB)
