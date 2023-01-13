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

    mag_data_X_mean = loaded['mag_data_X_mean']
    mag_data_Y_mean = loaded['mag_data_Y_mean']
    mag_data_Z_mean = loaded['mag_data_Z_mean']

    mag_data_X_sd = loaded['mag_data_X_sd']
    mag_data_Y_sd = loaded['mag_data_Y_sd']
    mag_data_Z_sd = loaded['mag_data_Z_sd']

    mag_data_X_mean_sub = loaded['mag_data_X_mean_sub']
    mag_data_Y_mean_sub = loaded['mag_data_Y_mean_sub']
    mag_data_Z_mean_sub = loaded['mag_data_Z_mean_sub']



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

    mag_data_X = np.array(mag_data_X , dtype = float)/16
    mag_data_Y = np.array(mag_data_Y , dtype = float)/16
    mag_data_Z = np.array(mag_data_Z , dtype = float )/16

    mag_data_X_mean = np.mean(mag_data_X)
    mag_data_Y_mean = np.mean(mag_data_Y)
    mag_data_Z_mean = np.mean(mag_data_Z)

    mag_data_X_sd = np.std(mag_data_X)
    mag_data_Y_sd = np.std(mag_data_Y)
    mag_data_Z_sd = np.std(mag_data_Z)

    mag_data_X_mean_sub = mag_data_X - mag_data_X_mean
    mag_data_Y_mean_sub = mag_data_Y - mag_data_Y_mean
    mag_data_Z_mean_sub = mag_data_Z - mag_data_Z_mean




    np.savez('outfile', mag_data_X=mag_data_X, mag_data_Y= mag_data_Y,mag_data_Z=mag_data_Z , mag_data_X_mean= mag_data_X_mean, mag_data_Y_mean=mag_data_Y_mean , mag_data_Z_mean=mag_data_Z_mean , mag_data_X_sd = mag_data_X_sd , mag_data_Y_sd=mag_data_Y_sd , mag_data_Z_sd=mag_data_Z_sd  , mag_data_X_mean_sub = mag_data_X_mean_sub , mag_data_Y_mean_sub= mag_data_Y_mean_sub , mag_data_Z_mean_sub = mag_data_Z_mean_sub )


print(mag_data_X_mean)
print(mag_data_Y_mean)
print(mag_data_Z_mean)


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

    xyHeading = math.atan2(float(mag_read[0]),  float(mag_read[1]))
    zxHeading = math.atan2(float(mag_read[2]), float(mag_read[0]))
    heading = xyHeading

    if (heading < 0):
        heading += 2 * math.pi
    
    if (heading > 2 * math.pi): 
        heading -= 2 * math.pi
        
    headingDegrees = heading * 180 / math.pi;
    xyHeadingDegrees = xyHeading * 180 / math.pi;
    zxHeadingDegrees = zxHeading * 180 / math.pi;

    print("Heading: " , end='');
    print(headingDegrees);





