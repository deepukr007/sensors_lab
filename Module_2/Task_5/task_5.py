import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import math

x = input()

if(x=='l'):

    loaded = np.load('outfile.npz')

    mag_data_X = loaded['mag_data_X']
    mag_data_Y = loaded['mag_data_Y']
    mag_data_Z = loaded['mag_data_Z']



else:
    serial_obj = serial.Serial('COM8', 115200 , timeout=1)
    time.sleep(1)
    serial_obj.flush()
    serial_obj.write("r".encode())
    time.sleep(3)

    mag_data_X = []
    mag_data_Y = []
    mag_data_Z = []

    
    while (len(mag_data_X)<=100):
                mag_read = serial_obj.readline()
                if (mag_read):
                    mag_read = mag_read.decode().strip().split(',')
                    mag_data_X.append(float(mag_read[0]))
                    mag_data_Y.append(float(mag_read[1]))
                    mag_data_Z.append(float(mag_read[2]))
             

    serial_obj.close()

    mag_data_X = np.array(mag_data_X , dtype = float)
    mag_data_Y = np.array(mag_data_Y , dtype = float)
    mag_data_Z = np.array(mag_data_Z , dtype = float )

    

    np.savez('outfile', mag_data_X=mag_data_X, mag_data_Y= mag_data_Y,mag_data_Z=mag_data_Z )


print("Calibration done")

value_x_min = np.min(mag_data_X)
value_x_max = np.max(mag_data_X)
value_y_min = np.min(mag_data_Y)
value_y_max = np.max(mag_data_Y)
value_z_min = np.min(mag_data_Z)
value_z_max = np.max(mag_data_Z)

value_offset_x = value_x_min + (value_x_max - value_x_min) / 2
value_offset_y = value_y_min + (value_y_max - value_y_min) / 2
value_offset_z = value_z_min + (value_z_max - value_z_min) / 2

print("Offsets")
print(value_offset_x)
print(value_offset_y)
print(value_offset_z)


serial_obj = serial.Serial('COM8', 115200 , timeout=1)
time.sleep(1)
serial_obj.flush()
serial_obj.write("r".encode())
time.sleep(3)


while(1):       
    mag_read = serial_obj.readline()
    if (mag_read):
        mag_read = mag_read.decode().strip().split(',')

    value_x = float(mag_read[0]) -value_offset_x
    value_y = float(mag_read[1]) -value_offset_y
    value_z = float(mag_read[2]) -value_offset_z

    xyHeading = math.atan2( value_y,value_x)
    zxHeading = math.atan2(value_z, value_x)
    heading = xyHeading

    if (heading < 0):
        heading += 2 * math.pi
    
    if (heading > 2 * math.pi): 
        heading -= 2 * math.pi
        
    headingDegrees = heading * 180 / math.pi

    print("Heading: " , end='')
    print(headingDegrees)





