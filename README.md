# Auto-play for the Jump Jump minigame in Penguin Isle mobile game

## Description

This program automatically detects two blobs (circular objects) in images, finds their center and finds the Euclidean distance between the two. It converts the distance into seconds to perform movments on an Arduino servo motor. 

This is aimed at video games that require pressing, holding and releasing to move from one object to another (e.g. the Jump Jump minigame ([YouTube](https://www.youtube.com/watch?v=C_E0wuMuVb4&pp=ygUWcGVuZ3VpbiBpc2xlIGp1bXAganVtcA%3D%3D)) which is part of the Penguin Isle mobile game ([iOS](https://apps.apple.com/hr/app/penguin-isle/id1474314811), [Android](https://play.google.com/store/apps/details?id=com.fantome.penguinisle&hl=en_US))).

### The procedure

The images are fed to the program by sharing the phone screen to a computer, where an image of the program that makes the process possible is taken. It performs image pre-processing and extracts the phone's screenshare from the full picture to reduce the working area. This is done by looking for a green rectangle (which is automatically added) and extracts its contents. It further reduces the image by removing 1/4 of the top and around 1/4 of the bottom. This is our working area.

After converting the image to black and white and performing morphological dilation, Canny edge detector finds all the edges. Then, blob detection runs twice: once for finding the source and once for the destination. To find the destination, it looks for an almost-perfect blob (since there are no objects breaking the surface shape). To find the source, it tolerates convexity to account for the characters breaking surface shape.

Euclidean distance is calculated from the source to the destination, and the result is converted into seconds. The conversion formula is found by trial and error. Finally, the seconds are sent to and Arduino Serial which are read and converted into movement by a servo motor.

## Getting Started

### Dependencies

* Requires [Arduino Software](https://www.arduino.cc/en/software)
* Requires [Arduino Uno](https://store.arduino.cc/products/arduino-uno-rev3) microcontroller or equivalent, servo motor, green and red LED lights
* Requires a screensharing software or web version of it (e.g. [Zoom](https://zoom.us/))
* Required packages: see `requirements.txt`
* Developed with Python 3.11.4

### Executing program and setting up environment

1. Set up your screensharing software. Make sure you have selected the appropriate window name of the screensharing software in the code. Make sure the software applies a green box around the device's screenshare, otherwise it won't find the screen. For best results, use [Zoom's web version](https://pwa.zoom.us/wc/).
2. Set up your microcontroller with the servo motor. Connect the servo motor to pin 9. Connect green and red LEDs to pin 3 and 5, respectively. Extend a cable from 3.3V on the microcontroller to your chosen DIY phone pen (this project uses a damp q-tip wrapped in alumninium foil). This simulates touches on the screen and should be scurely tied to the servo arm.
3. Open the terminal in the root directory of this project and run `python main.py`. To continue on the next execution, close the current image popups. To stop the execution, press CTRL + C.

### Changing the data

* Set the name of the screenshare program: go to `main.py` and change `Zoom - Google Chrome` to the target window name in `screenshot = get_image_from_software("Zoom - Google Chrome")`. The window name must be exactly as it is written on the program itself.
* Set the angle of the servo movement: go to `arduino\servo\servo.ino` and change the degrees for: `const int servoUp = 0; const int servoDown = 20;` The values must be in degrees and between 0° and 180°.
*  Set the port and the baud rate: go to `python\arduino_serial_operations\serial_operations.py` and set the port and baud rate in: `self.ser = Serial(port="COM3", baudrate=9600)`. Or you can call the class with `ArduinoSerial.set_port()` and `ArduinoSerial.set_baud_rate()`.
*  Disable automatic detection of blobs to manually select them: in `main.py` set the following two lines to `True`: `screen_img.find_source(manual=False) screen_img.find_destination(manual=False)`.

## Help
* The Arduino board is not connecting to the software: check if the appropriate board is selected under Arduino software -> Tools -> Board.
* The error "Window "_window_name_" does not exist." is raised: make sure the name of the software used to share your phone's screen to your computer is written exactly as it is. The window should also be active (e.g. when having multiple browser tabs open, only one of them will show as active. Click on the screensharing window to make that tab active).

## References:

* Massimo Banzi, David Cuartielles, Tom Igoe, David Mellis, "ARDUINO," 2023. [Online]. Available: https://www.arduino.cc/
* "Penguin Isle," Habby, 2023. [Online]. Available: https://www.facebook.com/penguinisle/
* A. Channel, "ペンギンの島　ジャンペン　Penguin Isle Jump!," YouTube, 21 April 2021. [Online]. Available: https://www.youtube.com/watch?v=C_E0wuMuVb4. [Accessed 15 July 2023].
* E. Yuan, "Zoom," Zoom Video Communications, Inc., 2023. [Online]. Available: https://zoom.us/
