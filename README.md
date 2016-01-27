# PiLogic

## Synopsis
Simple python program to get logic statement from the user and run the simplified version on the GPIO pins of a Raspberry Pi.

## Prerequisites
For this project, the user needs a functional Raspberry Pi, a breadboard, four switches, breadboarding wires, an LED + resistor, and a display/keyboard combo for RPI interaction.

## Use
To run the program, run the converter.py file as a super user using the command below:

	$ sudo python converter/converter.py

Next, enter in your logic statement with up to four inputs. Available characters include: A, B, C, D (letters are inputs), & (and), | (or), ~ (not), and parenthesis. some examples of acceptable logic statements include, '~A & C', 'A & (B | C)', and '(D & A) & (D | B) | (A & (D & C))'. Make sure you leave spaces between inputs and operators or you will throw errors in the program. After this step, the simplified version of the logic statement will be shown on screen and the Pi will start emulating the circuit using four switches (see program for pins used and the pinout guide for wiring help) and the LED to show the result of the current inputs.

## License
This setup guide is open and is licensed under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) for your use, modification, and distribution.
