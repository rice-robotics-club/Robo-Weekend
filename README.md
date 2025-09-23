# Robo-Weekend
Obv this repo needs WAY better documentation but its fiiiiine we ball - I'll fill in more info as we go! :)
Note: If you're familiar with Git / Github, you can clone this repo Clone then open in vscode with the extension installed and it will auto-boot into a pi pico project with all these files for easy use.

## Setup Guide:

### Installation
This guide should show you a set-by-set tutorial to setting up your Pi Pico with VSCode (The IDE we will be coding the robot with!): https://randomnerdtutorials.com/raspberry-pi-pico-vs-code-micropython/
NOTE: This tutorial uses Pico-W-Go instead of VSCode's official dedicated plugin for Pi Picos. As the official plugin is much better, we will be using it instead!

Aternatively:
1. Install VSCode: https://code.visualstudio.com/download
2. Download Python: https://www.python.org/downloads/
3. Download Raspberry Pi Pico MicroPython Configuration File (UF2). Get the latest version here: https://micropython.org/download/RPI_PICO/

### Setting up VSCODE
Once you've downloaded VSCode, we need to install an extension that allows vscode to interact with Pi Picos:
1. Navigate to VSCode plugins & Type in "Pi Pico"
2. Install the official "Raspberry Pi Pico" plugin
<img width="1916" height="990" alt="image" src="https://github.com/user-attachments/assets/461d74ad-0649-4dc3-9f14-2771137dec25" />
3. ACTIVATE AUTOSAVE PLEASE OH MY LORD IT WILL SAVE YOU FROM SO MUCH PAIN
<img width="612" height="876" alt="image" src="https://github.com/user-attachments/assets/44fc8d2f-b226-4202-9700-9fbedaf17e96" />

### Configuring Pi Pico
To get the pi pico board in bootloader mode (ready for us to configure it to use micropython), hold down the BOOTSEL button while plugging the board into USB. The uf2 file that we downloaded should then be copied to the USB mass storage device that appears (New drive in file explorer named RPI-RP5 or smthn). Once programming of the new firmware is complete the device will automatically reset and be ready for use! Just unplug and replug.

## Blink the Pi Pico
VSCode's extension for Pi Pico makes working with pico embedded systems so much easier.
1. Navigate to the Pi Pico plugin and create a new Pi Pico Project
<img width="1929" height="971" alt="image" src="https://github.com/user-attachments/assets/b02f4978-14e8-492d-8cef-49ba3404a943" />
Then, plug in your pico and it will auto detect it. In order to run your files on the pico, r-click on a file and select "Run current file on Pico". Note that if you ever hit control-c while a program is running, the pi needs to be restarted (unplug & replug, or disconnect & reconnect) - ALSO if you don't have autosave and forget to save your changes, NOTHING WILL BE UPLOADED TO THE PICO AND IT WON'T TELL YOU.

Start by running the blink.py file! When you run it, your Pi Pico's LED should start flashing on and off in an infinite loop.
<img width="1182" height="988" alt="image" src="https://github.com/user-attachments/assets/3bf3d94f-4951-48fc-91b9-7312e9e1c7f6" />

## Getting your servos & motors to move
We recommend you look through the elec slides before this section so you understand the basic concepts of wiring, breadboards, and pins.




