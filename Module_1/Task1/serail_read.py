import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x = []
y = []
z = []

source = input ()

if(source=='l'):

    loaded = np.load('outfile.npz')
    x = loaded['x']
    y = loaded['y']
    z = loaded['z']

    x_mean = loaded['x_mean']
    y_mean = loaded['y_mean']
    z_mean = loaded['z_mean']

    x_sd = loaded['x_sd']
    y_sd = loaded['y_sd']
    z_sd = loaded['z_sd']

    x_sub = loaded['x_sub']
    y_sub = loaded['y_sub']
    z_sub = loaded['z_sub']



else:

    serial_obj = serial.Serial('COM7', 115200 , timeout=1)
    time.sleep(2)
    flag = True

    
    while (flag):
            xyz_data = serial_obj.readline()
            if (xyz_data):
                xyz_data = xyz_data.decode().strip().split(',')
                print(xyz_data)

                if ( xyz_data[0] == "end"):
                    flag = False
                else:
                    x.append(float(xyz_data[0]))
                    y.append(float(xyz_data[1]))
                    z.append(float(xyz_data[2])) 
                

    serial_obj.close()

    x = np.array(x , dtype = float)
    y = np.array(y , dtype = float)
    z = np.array(z , dtype = float )

    x_mean = np.mean(x)
    y_mean = np.mean(y)
    z_mean = np.mean(z)

    x_sd = np.std(x)
    y_sd = np.std(y)
    z_sd = np.std(z)


    x_sub = x - x_mean
    y_sub = y - y_mean
    z_sub = z - z_mean


    np.savez('outfile', x=x, y=y ,z=z , x_sub=x_sub , y_sub=y_sub ,z_sub=z_sub , x_mean= x_mean, y_mean=y_mean , z_mean=z_mean ,x_sd=x_sd , y_sd=y_sd , z_sd=z_sd )


print (x)
print (y)
print (z)

print (x_mean)
print (y_mean)
print (z_mean)


print (x_sd)
print (y_sd)
print (z_sd)

print (x_sub)
print (y_sub)
print (x_sub)


plt.figure(1)
_, bins,_ =plt.hist(x_sub , bins=18, density=True )
m, s = norm.fit(x_sub)
p = norm.pdf(bins, m, s) 
plt.plot(bins, p, 'r', alpha=.5)
plt.xlabel('x-x_mean')
plt.ylabel('Frequency of values')
plt.title('Histogram : x - x_mean')
plt.savefig('hist_xsubt')

plt.figure(2)
_,bins,_=plt.hist(y_sub , bins='auto', density=True)
m, s = norm.fit(y_sub)
p = norm.pdf(bins, m, s) * 2
plt.plot(bins, p, 'r', alpha=.5)
plt.xlabel('y-y_mean')
plt.ylabel('Frequency of values')
plt.title('Histogram : y - y_mean')
plt.savefig('hist_ysubt')


plt.figure(3)
_, bins ,_ = plt.hist(z_sub , bins='auto', density=True)
m, s = norm.fit(z_sub)
p = norm.pdf(bins, m, s) * 2
plt.plot(bins, p, 'r', alpha=.5)
plt.xlabel('z-z_mean')
plt.ylabel('Frequency of values')
plt.title('Histogram : z - z_mean')
plt.savefig('hist_zsubt')

range = (np.arange(0 , (x.size*100) , 100))/1000


plt.figure(4)
plt.plot(range, x , color = 'green')
plt.plot(range, y ,color = 'blue' )
plt.plot(range , z , color = 'red')
plt.xlabel('Time in s')
plt.ylabel('Acceleration in m/s^2')
plt.title('Acceleration')
plt.legend(["x", "y" ,"z"] , loc="upper right")
plt.savefig('xyz_data')



plt.show() 