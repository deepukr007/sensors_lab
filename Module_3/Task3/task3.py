import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from datetime import datetime , timedelta
import matplotlib.dates as mdates

ex_name = input('Exp_name : ')
file = 'outfile' + ex_name +'.npz'

x = input()


def scale_down(values, min_val, max_val):
    """
    Scales down a list of values between a specified minimum and maximum.
    
    Args:
        values (list): A list of numeric values.
        min_val (float): The minimum value of the scaled down range.
        max_val (float): The maximum value of the scaled down range.
    
    Returns:
        list: A list of scaled down values.
    """
    max_input = max(values)
    min_input = min(values)
    range_input = max_input - min_input
    range_output = max_val - min_val
    scaled_values = [((x - min_input) / range_input) * range_output + min_val for x in values]
    return scaled_values

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

    total_read = (24*60*60)/30


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




time_str = '06::30::30'
time_object = datetime.strptime(time_str, '%H::%M::%S')
x_range = []

for i in range(2880):
    delta = timedelta(seconds= 30)
    time_object = time_object + delta
    x_range.append(time_object)

range = np.arange(30 , (2880*30)+30, 30 , dtype=float)/3600
xformatter = mdates.DateFormatter('%H:%M')

temp = scale_down(co2,27.2 ,25)
humidity = scale_down(co2,28 ,27)


plt.figure(1)
plt.plot( x_range , iaq, color = 'green' , label="iaq")
plt.plot(x_range , co2 , color = 'blue' , label="co2 concentration")
plt.plot(x_range , temp , color = 'red' , label="temperature")
plt.plot(x_range , humidity , color = 'black' , label="humidity")

plt.rcParams["figure.autolayout"] = True
plt.xlabel('Timestamp')
plt.ylabel("IAQ" )
plt.title('IAQ readings')
plt.legend(loc='upper left')
plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
plt.savefig('new'+'IAQ' )



plt.show() 
