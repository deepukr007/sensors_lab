import serial
import time
import matplotlib.pyplot as plt
import numpy as np

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

    
    while (len(mag_data_X)<=1000):
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




plt.figure(1)
_, bins,_ = plt.hist(mag_data_X_mean_sub , bins=20 , density=True)
plt.xlabel('x-x_mean')
plt.ylabel('Frequency of values')
plt.title('Histogram : x - x_mean')
plt.savefig('hist_xsubt')

plt.figure(2)
_, bins,_ =plt.hist(mag_data_Y_mean_sub , bins=20 , density=True)
plt.xlabel('y-y_mean')
plt.ylabel('Frequency of values')
plt.title('Histogram : y - y_mean')
plt.savefig('hist_ysubt')

plt.figure(3)
_, bins,_ =plt.hist(mag_data_Z_mean_sub , bins=25 , density=True)
plt.xlabel('z-z_mean')
plt.ylabel('Frequency of values')
plt.title('Histogram : z - z_mean')
plt.savefig('hist_zsubt')

range = (np.arange(0 , (mag_data_X.size*100) , 100))/1000

plt.figure(4)
plt.plot(range , mag_data_X , color = 'green')
plt.plot(range , mag_data_Y ,color = 'blue' )
plt.plot(range , mag_data_Z , color = 'red')
plt.xlabel('Time in s')
plt.ylabel('-')
plt.title('-')
plt.legend(["x", "y" ,"z"] , loc="upper right")
plt.savefig('xyz_data')



plt.show() 