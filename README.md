# Auto-play for the Jump Jump minigame in Penguin Isle app

## Description

This program automatically detects two blobs (circular objects) in images, finds their center and finds the Euclidean distance between the two. It converts the distance into seconds to perform movments on an Arduino servo motor. 

This is aimed at video games that require pressing, holding and releasing to move from one object to another (e.g. the Jump Jump minigame ([YouTube](https://www.youtube.com/watch?v=C_E0wuMuVb4&pp=ygUWcGVuZ3VpbiBpc2xlIGp1bXAganVtcA%3D%3D)) in the Penguin Isle mobile game ([iOS](https://apps.apple.com/hr/app/penguin-isle/id1474314811), [Android](https://play.google.com/store/apps/details?id=com.fantome.penguinisle&hl=en_US))).

### The procedure

The images are fed to the program by sharing the phone screen to a computer, where an image of the program that makes the process possible is taken. It performs image pre-processing and extracts the phone's screenshare from the full picture to reduce the working area. This is done by looking for a green rectangle (which is automatically added) and extracts its contents. It further reduces the image by removing 1/4 of the top and around 1/4 of the bottom. This is our working area.

After converting the image to black and white and performing morphological dilation, Canny edge detector finds all the edges. Then, blob detection runs twice: once for finding the source and once for the destination. To find the destination, it looks for an almost-perfect blob (since there are no objects breaking the surface shape). To find the source, it tolerates convexity to account for the characters breaking surface shape.

Euclidean distance is calculated from the source to the destination, and the result is converted into seconds. The conversion formula is found by trial and error. Finally, the seconds are sent to and Arduino Serial which are read and converted into movement by a servo motor.

## Getting Started

### Dependencies

* Required packages: 
* Developed with Python X

### Executing program



### Changing the data

* Set the name of the screenshare program: go to `main.py` and change `"Zoom - Google Chrome"` to the target window name in `screenshot = get_image_from_software("Zoom - Google Chrome")`. The window name must be exactly as it is written on the program itself.
* Set the angle of the servo movement: go to `arduino\servo\servo.ino` and change the degrees for: `const int servoUp = 0; const int servoDown = 20;` The values must be in degrees and between 0° and 180°.
*  Set the port and the baud rate: go to `python\arduino_serial_operations\serial_operations.py` and set the port and baud rate in: `self.ser = Serial(port="COM3", baudrate=9600)`. Or you can call the class with `ArduinoSerial.set_port()` and `ArduinoSerial.set_baud_rate()`.
*  
*  

### Making use of other tools



## Help
* If the Arduino board is not connecting to the software: check if the appropriate board is selected under Arduino software -> Tools -> Board.
