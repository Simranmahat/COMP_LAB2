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

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy(),0,len(arr)-1)
    end_time = time.time()
    return end_time - start_time

start_time = current_time()
increment_size = 50
best_time_array_quick = []
worst_time_array_quick=[]
worst_time_array_merge = []
best_time_array_merge=[]
MAX_ARRAY_SIZE=80

for i in range(MAX_ARRAY_SIZE):
    increment_size +=10
    array = generate_random_array(0,increment_size)
    sorted_input = sorted(array)
    reversed_input = sorted_input[::-1]
     #Measure Quick Sort time
    best_time_array_quick.append(measure_time(quick, array.copy()))
    worst_time_array_quick.append(measure_time(quick, reversed_input.copy()))
    # Measure Merge Sort times
    best_time_array_merge.append(measure_time(MergeSort, sorted_input.copy()))
    worst_time_array_merge.append(measure_time(MergeSort, reversed_input.copy()))
  
plt.plot(best_time_array_merge, label='BestCaseMerge Sort')
plt.plot(best_time_array_quick, label='BestCaseQuick Sort')
plt.plot(worst_time_array_merge, label='WorstCaseMerge Sort')
plt.plot(worst_time_array_quick, label='WorstCaseQuick Sort')
plt.xlabel('Array Size(array size)')
plt.ylabel('Time(Second)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.show()
