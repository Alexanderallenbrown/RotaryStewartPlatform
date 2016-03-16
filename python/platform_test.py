import serial
from numpy import *
import time
from matplotlib.pyplot import *

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=serial.XOFF,
    rtscts=False,
    dsrdtr=False
)

starttime = time.time()

ser.close()
ser.open()
while ser.isOpen():
	timenow = time.time()-starttime
	command = [0,0,int(10*sin(timenow)),0,0,0]
	ser.write('6')
	for ind in range(0,len(command)):
		ser.write(bytes(command[ind]))
	print timenow,command
	time.sleep(0.1)

