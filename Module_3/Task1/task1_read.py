import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

ex_name = input('Exp_name')
file = 'outfile' + ex_name +'.npz'

x = input()

if(x=='l'):
    loaded = np.load(file)
    gas = loaded['gas']

else:
    serial_obj = serial.Serial('COM8', 115200 , timeout=1)
    time.sleep(1)
    serial_obj.flush()
    serial_obj.write("r".encode())
    time.sleep(3)
    
    gas = []
    
    while (len(gas)<=60):
                gas_read = serial_obj.readline()
                if (gas_read):
                    gas_read = gas_read.decode().strip()
                    print(gas_read)
                    gas.append(float(gas_read))
             

    serial_obj.close()
    gas = np.array(gas , dtype = float)
 
    np.savez(file,gas=gas )


range = (np.arange(0 , (gas.size*100) , 100))/1000

plt.figure(4)
plt.plot(range , gas , color = 'red')
plt.xlabel('Time in s')
plt.ylabel("Resitance" )
plt.title('Gas sensor readings')
plt.savefig('Gas_sensor_readings')

plt.show() 