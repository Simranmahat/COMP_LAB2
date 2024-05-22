import random
import time
from merge import MergeSort
from merge import Merge
from Quicksort import partition
from Quicksort import quick

import matplotlib.pyplot as plt

def current_time():
    return time.time()

def cal_time(start_time,end_time):
    result=end_time-start_time
    return result

def generate_random_array(start_range, end_range):
    if end_range == 0 or start_range >= end_range:
        return []
    return [random.randint(start_range, end_range) for _ in range(end_range-start_range)]


start_time = current_time()
increment_size = 10
time_array_quick = []
time_array_merge=[]
MAX_ARRAY_SIZE=90
for i in range(MAX_ARRAY_SIZE):
    increment_size +=5
    array = generate_random_array(0,increment_size)

    start_time = current_time()
    MergeSort(array,0,len(array)-1)
    end_time = current_time()
    time_array_merge.append(cal_time(start_time, end_time))
    

    start_time = current_time()
    quick(array,0, len(array)-1)
    end_time = current_time()
    time_array_quick.append(cal_time(start_time, end_time))


   
plt.plot(time_array_merge, label='Merge Sort')
plt.plot(time_array_quick, label='Quick Sort')

plt.xlabel('Array Size(array size)')
plt.ylabel('Time(Second)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.show()
