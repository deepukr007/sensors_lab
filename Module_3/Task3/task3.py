import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from datetime import datetime

ex_name = input('Exp_name : ')
file = 'outfile' + ex_name +'.npz'

x = input()


if(x=='l'):
    loaded = np.load(file)
    iaq = loaded['iaq'] 
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


    print("Accuracy 3 reached at" , end = '  ' )
    print(datetime.now().hour , end=":")
    print(datetime.now().minute)


    iaq_list = []
    co2_list=[]
    accuracy_list= []
    hou_list =[]
    minute_list = []

    total_read = (24*60*60)/10


    while (len(iaq_list)<= total_read):
                gas_read = serial_obj.readline()
                if (gas_read):
                    gas_read = gas_read.decode().strip().split(',')
                    print(gas_read)
                    iaq_list.append(float(gas_read[0]))
                    co2_list.append(float(gas_read[1]))
                    accuracy_list.append(float(gas_read[2]))

                    iaq = np.array(iaq_list , dtype = float)
                    co2 = np.array(co2_list , dtype = float)
                    accuracy = np.array(accuracy_list , dtype = float)
                    now=datetime.now()
                    hour_now= now.hour
                    minute_now = now.minute
                    hou_list.append(hour_now)
                    minute_list.append(minute_now)
                    hour = np.array(hou_list , dtype=int)
                    minute = np.array(minute_list , dtype=int)

                
                    np.savez(file,iaq=iaq , co2 = co2 )
             

    serial_obj.close()





range = np.arange(30 , (2880*30)+30, 30 , dtype=float)/3600


plt.figure(1)
plt.plot( range , iaq, color = 'red')
plt.rcParams["figure.autolayout"] = True
plt.xticks(np.arange(0,25))
plt.xlabel('Time in m')
plt.ylabel("IAQ" )
plt.title('Gas sensor readings')
plt.savefig('new'+'IAQ' )


plt.show() 

plt.figure(2)
plt.plot(range , co2 , color = 'blue')
plt.rcParams["figure.autolayout"] = True
plt.xticks(np.arange(0,25))
plt.xlabel('Time in s')
plt.ylabel("Co2" )
plt.title('Gas sensor readings')
plt.savefig(ex_name+'co2')

plt.show() 