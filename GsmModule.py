import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)   

# Enable Serial Communication
port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout = 1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write(b'AT\r\n')
time.sleep(1)
rcv = port.read(10)
print(rcv)

port.write(b'AT+CFUN=1\r\n')
time.sleep(2)
rcv = port.read(50)
print(rcv)

port.write(b'AT+CMGF=1\r\n')
time.sleep(2)
rcv = port.read(50)
print(rcv)

port.write(b'AT+CNMI=2,1,0,0,0\r\n')
time.sleep(2)
rcv = port.read(50)
print(rcv)

port.write(b'AT+CMGS="09639003162"\r\n')
time.sleep(2)
rcv = port.read(50)
print(rcv)

msg = "hello"
port.reset_output_buffer()
time.sleep(1)
port.write(str.encode(msg + chr(26)))
time.sleep(2)
rcv = port.read(50)
print(rcv)