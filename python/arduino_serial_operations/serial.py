import serial
import time


class Serial:
    def __init__(self, port='COM3', baud_rate=9600):
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(2)

    def set_port(self, port: str):
        self.ser.port = port

    def set_baud_rate(self, baud_rate: int):
        self.ser.baudrate = baud_rate

    def write_to_serial(self, text: str):
        self.ser.write(text.encode('utf-8'))
