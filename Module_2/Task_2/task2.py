import serial
import time
import matplotlib.pyplot as plt
import numpy as np

x = input()


if(x=='l'):

    loaded = np.load('outfile.npz')

    bf_mag_data_X = loaded['bf_mag_data_X']
    bf_mag_data_Y = loaded['bf_mag_data_Y']
    bf_mag_data_Z = loaded['bf_mag_data_Z']

    bf_mag_data_X_mean = loaded['bf_mag_data_X_mean']
    bf_mag_data_Y_mean = loaded['bf_mag_data_Y_mean']
    bf_mag_data_Z_mean = loaded['bf_mag_data_Z_mean']

    bf_mag_data_X_sd = loaded['bf_mag_data_X_sd']
    bf_mag_data_Y_sd = loaded['bf_mag_data_Y_sd']
    bf_mag_data_Z_sd = loaded['bf_mag_data_Z_sd']

    bf_mag_data_X_mean_sub = loaded['bf_mag_data_X_mean_sub']
    bf_mag_data_Y_mean_sub = loaded['bf_mag_data_Y_mean_sub']
    bf_mag_data_Z_mean_sub = loaded['bf_mag_data_Z_mean_sub']

    af_mag_data_X = loaded['af_mag_data_X']
    af_mag_data_Y = loaded['af_mag_data_Y']
    af_mag_data_Z = loaded['af_mag_data_Z']

    af_mag_data_X_mean = loaded['af_mag_data_X_mean']
    af_mag_data_Y_mean = loaded['af_mag_data_Y_mean']
    af_mag_data_Z_mean = loaded['af_mag_data_Z_mean']

    af_mag_data_X_sd = loaded['af_mag_data_X_sd']
    af_mag_data_Y_sd = loaded['af_mag_data_Y_sd']
    af_mag_data_Z_sd = loaded['af_mag_data_Z_sd']

    af_mag_data_X_mean_sub = loaded['af_mag_data_X_mean_sub']
    af_mag_data_Y_mean_sub = loaded['af_mag_data_Y_mean_sub']
    af_mag_data_Z_mean_sub = loaded['af_mag_data_Z_mean_sub']



else:

    serial_obj = serial.Serial('COM8', 115200 , timeout=1)
    time.sleep(1)
    serial_obj.flush()
    serial_obj.write("r".encode())
    time.sleep(3)

    bf_mag_data_X = []
    bf_mag_data_Y = []
    bf_mag_data_Z = []

    
    while (len(bf_mag_data_X)<=100):
                bf_mag_read = serial_obj.readline()
                if (bf_mag_read):
                    bf_mag_read = bf_mag_read.decode().strip().split(',')
                    bf_mag_data_X.append(float(bf_mag_read[0]))
                    bf_mag_data_Y.append(float(bf_mag_read[1]))
                    bf_mag_data_Z.append(float(bf_mag_read[2]))
             

    serial_obj.close()

    bf_mag_data_X = np.array(bf_mag_data_X , dtype = float)/16
    bf_mag_data_Y = np.array(bf_mag_data_Y , dtype = float)/16
    bf_mag_data_Z = np.array(bf_mag_data_Z , dtype = float )/16

    bf_mag_data_X_mean = np.mean(bf_mag_data_X)
    bf_mag_data_Y_mean = np.mean(bf_mag_data_Y)
    bf_mag_data_Z_mean = np.mean(bf_mag_data_Z)

    bf_mag_data_X_sd = np.std(bf_mag_data_X)
    bf_mag_data_Y_sd = np.std(bf_mag_data_Y)
    bf_mag_data_Z_sd = np.std(bf_mag_data_Z)

    bf_mag_data_X_mean_sub = bf_mag_data_X - bf_mag_data_X_mean
    bf_mag_data_Y_mean_sub = bf_mag_data_Y - bf_mag_data_Y_mean
    bf_mag_data_Z_mean_sub = bf_mag_data_Z - bf_mag_data_Z_mean


    print("After flipping")

    input("Enter sometthig to proceed")


    serial_obj = serial.Serial('COM8', 115200 , timeout=1)
    time.sleep(3)

    af_mag_data_X = []
    af_mag_data_Y = []
    af_mag_data_Z = []

    
    while (len(af_mag_data_X)<=100):
                af_mag_read = serial_obj.readline()
                if (af_mag_read):
                    af_mag_read = af_mag_read.decode().strip().split(',')
                    af_mag_data_X.append(float(af_mag_read[0]))
                    af_mag_data_Y.append(float(af_mag_read[1]))
                    af_mag_data_Z.append(float(af_mag_read[2]))
             

    serial_obj.close()

    af_mag_data_X = np.array(af_mag_data_X , dtype = float)/16
    af_mag_data_Y = np.array(af_mag_data_Y , dtype = float)/16
    af_mag_data_Z = np.array(af_mag_data_Z , dtype = float )/16

    af_mag_data_X_mean = np.mean(af_mag_data_X)
    af_mag_data_Y_mean = np.mean(af_mag_data_Y)
    af_mag_data_Z_mean = np.mean(af_mag_data_Z)

    af_mag_data_X_sd = np.std(af_mag_data_X)
    af_mag_data_Y_sd = np.std(af_mag_data_Y)
    af_mag_data_Z_sd = np.std(af_mag_data_Z)

    af_mag_data_X_mean_sub = af_mag_data_X - af_mag_data_X_mean
    af_mag_data_Y_mean_sub = af_mag_data_Y - af_mag_data_Y_mean
    af_mag_data_Z_mean_sub = af_mag_data_Z - af_mag_data_Z_mean

    np.savez('outfile', bf_mag_data_X=bf_mag_data_X, bf_mag_data_Y= bf_mag_data_Y,bf_mag_data_Z=bf_mag_data_Z , 
    bf_mag_data_X_mean= bf_mag_data_X_mean, bf_mag_data_Y_mean=bf_mag_data_Y_mean , bf_mag_data_Z_mean=bf_mag_data_Z_mean , 
    bf_mag_data_X_sd = bf_mag_data_X_sd , bf_mag_data_Y_sd=bf_mag_data_Y_sd , bf_mag_data_Z_sd=bf_mag_data_Z_sd  , 
    bf_mag_data_X_mean_sub = bf_mag_data_X_mean_sub , bf_mag_data_Y_mean_sub= bf_mag_data_Y_mean_sub , 
    bf_mag_data_Z_mean_sub = bf_mag_data_Z_mean_sub,
    af_mag_data_X=af_mag_data_X, af_mag_data_Y= af_mag_data_Y,af_mag_data_Z=af_mag_data_Z , 
    af_mag_data_X_mean= af_mag_data_X_mean, af_mag_data_Y_mean=af_mag_data_Y_mean , af_mag_data_Z_mean=af_mag_data_Z_mean , 
    af_mag_data_X_sd = af_mag_data_X_sd , af_mag_data_Y_sd=af_mag_data_Y_sd , af_mag_data_Z_sd=af_mag_data_Z_sd  , 
    af_mag_data_X_mean_sub = af_mag_data_X_mean_sub , af_mag_data_Y_mean_sub= af_mag_data_Y_mean_sub , 
    af_mag_data_Z_mean_sub = af_mag_data_Z_mean_sub  )


print("Before")
print("X_mean", end=' ')
print(bf_mag_data_X_mean)
print("Y_mean", end=' ')
print(bf_mag_data_Y_mean)
print("Z_mean", end=' ')
print(bf_mag_data_Z_mean)
print("X_sd", end=' ')
print(bf_mag_data_X_sd)
print("Y_sd", end=' ')
print(bf_mag_data_Y_sd)
print("Z_sd", end=' ')
print(bf_mag_data_Z_sd)

print()

print("After")
print("X_mean", end=' ')
print(af_mag_data_X_mean)
print("Y_mean", end=' ')
print(af_mag_data_Y_mean)
print("Z_mean", end=' ')
print(af_mag_data_Z_mean)
print("X_sd", end=' ')
print(af_mag_data_X_sd)
print("Y_sd", end=' ')
print(af_mag_data_Y_sd)
print("Z_sd", end=' ')
print(af_mag_data_Z_sd)

print("Offest")
print("X", end=' ')
print(abs(bf_mag_data_X_mean - af_mag_data_X_mean))
print("Y", end=' ')
print(abs(bf_mag_data_Y_mean - af_mag_data_Y_mean))
print("Z", end=' ')
print(abs(bf_mag_data_Z_mean - af_mag_data_Z_mean))

