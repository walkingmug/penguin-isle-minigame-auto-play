import serial
import time


class Serial:
    def __init__(self, port='COM3', baud_rate=9600):
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(2)
    
    def set_baud_rate(self, baud_rate: int):
        self.baud_rate = baud_rate

    def set_port(self, port: str):
        self.port = port

    def write_to_serial(self, text: str):
        self.ser.write(text.encode('utf-8'))