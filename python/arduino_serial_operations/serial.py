import serial
import time


class Serial:
    def __init__(self, port='COM3', baud_rate=9600):
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(2)
    
    def write_to_serial(self, text: str):
        self.ser.write(text.encode('utf-8'))