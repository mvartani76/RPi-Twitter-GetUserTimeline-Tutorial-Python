import serial
import sys

ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.write(sys.argv[1])
