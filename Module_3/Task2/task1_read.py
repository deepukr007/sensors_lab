import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

ex_name = input('Exp_name : ')
file = 'outfile' + ex_name +'.npz'

x = input()

if(x=='l'):
    loaded = np.load(file)
    voc = loaded['voc']
    co2 = loaded['co2']

else:
    serial_obj = serial.Serial('/dev/cu.usbmodem21CBF3D62', 115200 , timeout=1)
    time.sleep(1)
    serial_obj.flush()
    serial_obj.write("r".encode())
    time.sleep(3)
    
    

    accuracy = 0
    while(accuracy!=3):
        read = serial_obj.readline()
        if(read):
            read =read.decode().strip().split(',')
            accuracy = int(read[2])
            print(read)

    input()


    voc = []
    co2 =[]
    accuracy= []

    while (len(voc)<=60):
                gas_read = serial_obj.readline()
                if (gas_read):
                    gas_read = gas_read.decode().strip().split(',')
                    print(gas_read)
                    voc.append(float(gas_read[0]))
                    co2.append(float(gas_read[1]))
                    accuracy.append(float(gas_read[2]))

             

    serial_obj.close()
    voc = np.array(voc , dtype = float)
    co2 = np.array(co2 , dtype = float)
    accuracy = np.array(accuracy , dtype = float)

 
    np.savez(file,voc=voc , co2 = co2 , accuracy = accuracy  )


range = np.arange(10 , (voc.size*10)+10, 10)/60

plt.figure(1)
plt.plot(range , voc , color = 'red')
plt.xlabel('Time in s')
plt.ylabel("VOC" )
plt.title('Gas sensor readings')
plt.savefig(ex_name+'voc' )

plt.figure(2)
plt.plot(range , co2 , color = 'blue')
plt.xlabel('Time in s')
plt.ylabel("Co2" )
plt.title('Gas sensor readings')
plt.savefig(ex_name+'co2')

plt.show() 