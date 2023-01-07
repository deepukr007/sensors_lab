import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

souce = input()

if(souce=='l'):

    loaded = np.load('outfile.npz')
    pressure = loaded['pressure']
    z = loaded['z']
    time = loaded['time']
    h_pa = loaded['h_pa']
    temp = loaded['temp']


else:
    serial_obj = serial.Serial('COM7', 115200 , timeout=1)
    time.sleep(1)

    time = []
    pressure = []
    z = []
    temp = []
    

    flag = True
    
    while (flag):
            data = serial_obj.readline()
            if (data):
                data = data.decode().strip().split(',')
                print(data)
                if ( data[0] == "end"):
                    flag = False
                else:
                    time.append(float(data[0]))
                    pressure.append(float(data[1]))
                    z.append(float(data[2]))
                    temp.append(float(data[3]))

    serial_obj.close()

        
    time = np.array(time , dtype = float)
    pressure = np.array(pressure , dtype = float)
    z = np.array(z , dtype = float)
    temp = np.array(temp , dtype = float)

    ratio = pressure / 1013.25
    h_pa = -1 * ( ( np.log(ratio) * temp[0] ) / .034)

    np.savez('outfile', pressure=pressure, time=time ,z=z , temp=temp,  h_pa = h_pa)


print (time)
print (pressure)
print (z)
print (temp)
print (h_pa)

z_mean = np.mean(z)
z_sub = z-z_mean

time_check = time / 1000 

velocity = integrate.cumulative_trapezoid(z_sub, time_check)

velocity_mean = np.mean(velocity)
velocity_sub = velocity - velocity_mean

accel_height =  integrate.cumulative_trapezoid(velocity_sub, time_check[1:])

ground_height = h_pa[1]

h_pa_ref = h_pa - ground_height
    
plt.figure(1)
plt.plot(time/1000 , pressure*100 , color = 'red')
plt.xlabel('Time in s')
plt.ylabel('Pressure in Pa')
plt.title('Pressure Sensor Values')
plt.savefig('pressure_values')

plt.figure(2)
plt.plot(time/1000 , z , color = 'green')
plt.xlabel('Time in s')
plt.ylabel('Accelearation in m/s^2')
plt.title('Acceleration Values')
plt.savefig('Accelearation Values')

plt.figure(3)
plt.plot(time/1000 , h_pa , color = 'green')
plt.xlabel('Time in s')
plt.ylabel('Height in m')
plt.title('Height V/s time ')
plt.savefig('HeightvsTime_pressure')

plt.figure(4)
plt.plot(time[1:]/1000,velocity)
plt.xlabel('Time in s')
plt.ylabel('Velocity in m/s')
plt.title('Velocity vs Time')
plt.savefig('Velocityvstime')


plt.figure(5)
plt.plot(time/1000 , h_pa_ref , color = 'blue')
plt.plot(time[2:]/1000, accel_height , color='green')
plt.xlabel('Time in s')
plt.ylabel('Heigt in m')
plt.title('Height v/s Time')
plt.legend(["Height from Pressure Sensor" , "Height from Accelerometer"] , loc="upper right")
plt.savefig('HeightvsTime')




plt.show() 