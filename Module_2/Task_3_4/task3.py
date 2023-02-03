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



print("Task_3")
print("Mean")
print("X" , end=' : ')
print(mag_data_X_mean)
print("Y" , end=': ')
print(mag_data_Y_mean)
print("Z" , end=': ')
print(mag_data_Z_mean)
print()
print("Standard Deviation")
print("X" , end='" ')
print(mag_data_X_sd)
print("Y" , end=': ')
print(mag_data_Y_sd)
print("Z" , end=': ')
print(mag_data_Z_sd)
print()



print("Task_4")
print()
print("Horizontal mag field" , end =": ")
print(math.sqrt(((mag_data_X_mean + 50.5)**2 + (mag_data_Y_mean + 29.5) **2)))
print("Vertical Mag field" , end=": ")
print(mag_data_Z_mean)
print("Total magnetic field", end=": ")
print(math.sqrt(((mag_data_X_mean + 50.5)**2 + (mag_data_Y_mean + 29.5)**2 + mag_data_Z_mean ** 2  )))

