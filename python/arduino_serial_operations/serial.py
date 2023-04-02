import serial
import time


class Serial:
    def __init__(self, port='COM3', baud_rate=9600):
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(2)