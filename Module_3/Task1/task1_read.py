import serial
import time
import matplotlib.pyplot as plt
import numpy as np

ex_name = input('Exp_name : ')
file = 'outfile' + ex_name + '.npz'

x = input()

if(x=='l'):
    loaded = np.load(file)
    gas = loaded['gas']

else:
    serial_obj = serial.Serial('/dev/cu.usbmodem0992BE7D2', 115200 , timeout=1)
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


range = (np.arange(0 , (gas.size)*10 , 10))

plt.figure(1)
plt.plot(range , gas , color = 'red')
plt.xlabel('Time in s')
plt.ylabel("Resitance in \u03A9" )
plt.title('Gas sensor readings for Perfume')
plt.savefig('Gas_sensor_readings_'+ ex_name)

plt.show() 