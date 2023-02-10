import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime , timedelta

time_str = '06::30::30'
time_object = datetime.strptime(time_str, '%H::%M::%S')

x_range = []

for i in range(2880):
    delta = timedelta(seconds= 30)
    time_object = time_object + delta
    x_range.append(time_object.time())