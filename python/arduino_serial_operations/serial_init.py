import serial
import time


def initialize_serial(port='COM3', baud_rate=9600):
    """Launches the Arduino serial for reading and writing.

    :param port: Port name. Check the port being used in Arduino under
     Tools -> Port. Defaults to 'COM3'.
    :param baud_rate: Set the speed of the serial communicator. 
     Defaults to 9600.
    :return: A serial object representing the serial port connection.
    """
    ser = serial.Serial(port, baud_rate)
    time.sleep(2)

    return ser