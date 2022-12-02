import serial
import time
import matplotlib.pyplot as plt
import numpy as np

x = input()

if(x=='l'):

    loaded = np.load('outfile.npz')
    pressure = loaded['pressure']
    pressure_mean = loaded['pressure_mean']
    pressure_sub = loaded['pressure_sub']
    pressure_sd = loaded['pressure_sd']


else:
    serial_obj = serial.Serial('COM7', 115200 , timeout=1)
    time.sleep(1)
    pressure = []

    flag = True
    
    while (flag):
            p_data = serial_obj.readline()
            if (p_data):
                p_data = p_data.decode().strip().split(',')
                print(p_data)
                if ( p_data[0] == "end"):
                    flag = False
                else:
                    pressure.append(float(p_data[0]) * 100)
                

    serial_obj.close()

        
    pressure = np.array(pressure , dtype = float)
    pressure_mean = np.mean(pressure)
    pressure_sub = pressure - pressure_mean
    pressure_sd = np.std(pressure)

    np.savez('outfile', pressure=pressure, pressure_sub=pressure_sub ,pressure_mean=pressure_mean , pressure_sd=pressure_sd)



print (pressure)
print (pressure_mean)
print (pressure_sd)
print (pressure_sub)


plt.figure(1)
plt.hist(pressure , bins='auto')
plt.xlabel('Pressure in Pa')
plt.ylabel('Frequency')
plt.title('Histogram of Pressure')
plt.savefig('hist_pressure')



plt.figure(2)
plt.hist(pressure_sub , bins='auto')
plt.xlabel('Mean subtracted values')
plt.ylabel('Frequency')
plt.title('Histogram of p-pmean')
plt.savefig('p-pmean')



range = (np.arange(0 , (pressure.size*100) , 100))/1000


plt.figure(3)
plt.plot(range, pressure , color = 'green')
plt.xlabel('Time in s')
plt.ylabel('Pressure in Pa')
plt.title('Pressure Sensor Values')
plt.savefig('pressure_values')


plt.show() 