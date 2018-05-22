import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
    
# import serial
# import time
# s = serial.Serial('COM5',9600)
# time.sleep(2)
# s.write('0'.encode())
# print('Open gate Successful')