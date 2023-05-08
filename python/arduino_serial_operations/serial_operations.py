"""Classes for connecting to and manipulating Arduino.
"""

from serial import Serial
import time


class ArduinoSerial:
    """Configures Arduino connection and communicates movements to the servo.
    """
    def __init__(self):
        self.ser = Serial(port='COM3', baudrate=9600)
        time.sleep(2)

    def set_port(self, port: str):
        self.ser.port = port

    def set_baud_rate(self, baud_rate: int):
        self.ser.baudrate = baud_rate

    def _move_servo_down(self):
        self.ser.write(b'1')

    def _move_servo_up(self):
        self.ser.write(b'0')

    def move_servo(self, duration: float):
        self._move_servo_down()
        print(duration)
        time.sleep(duration)
        self._move_servo_up()
