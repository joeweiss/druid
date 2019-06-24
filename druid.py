import sys
import serial
import readline

try:
  ser = serial.Serial("/dev/ttyACM0",115200, timeout=0.1)
except:
  print("serial problem with /dev/ttyACM0")
  exit()

cmd = ""

print("//// druid. q to quit.")

while cmd != "q":
  ser.write(cmd+"\r\n")
  print(ser.read(1000000))
  cmd = raw_input("> ")