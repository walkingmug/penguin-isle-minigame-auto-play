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
