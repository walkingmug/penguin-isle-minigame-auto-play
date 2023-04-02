from python.arduino_serial_operations.serial_init import initialize_serial
import serial
import time


def write_to_serial():
    ser = initialize_serial()