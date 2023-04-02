from serial import Serial
import time


class ArduinoSerial:
    def __init__(self):
        self.ser = Serial(port='COM3', baudrate=9600)
        time.sleep(2)

    def set_port(self, port: str):
        self.ser.port = port

    def set_baud_rate(self, baud_rate: int):
        self.ser.baudrate = baud_rate

    def write_to_serial(self, text: str):
        self.ser.write(text.encode('utf-8'))

    def _move_servo_down(self):
        self.write_to_serial("ServoDown")

    def _move_servo_up(self):
        self.write_to_serial("ServoUp")

    def move_servo(self, duration: float):
        self._move_servo_down()
        time.sleep(duration)
        self._move_servo_up