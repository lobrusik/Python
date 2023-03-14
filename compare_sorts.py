def bubble_sort(A, n):
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if A[j-1]>A[j]:
                A[j], A[j-1]=A[j-1], A[j]

def selection_sort(A, n):
    for i in range(0, n-1):
        k=i
        for j in range(i+1, n):
            if A[j]<A[k]:
                k=j
        A[k], A[i] = A[i], A[k]

def insertion_sort(A, n):
    for i in range(1,n):
        x=A[i]
        j=i-1
        while (j>=0 and x<A[j]):
            A[j+1]=A[j]
            j=j-1
        A[j+1]=x

import random
with open('arrays.txt', 'w') as f:
      for _ in range(100):
          array=[random.randint(-2000,2000) for _ in range(50)]
          f.write(' '.join(map(str,array))+'\n')
      f.close()

import time
def measure_time(sort_func):
    with open('arrays.txt', 'r') as f:
        start_time = time.perf_counter()
        for line in f:
            array=[int(x) for x in line.split()]
            sort_func(array, len(array))
        end_time = time.perf_counter()
    f.close()
    return (end_time - start_time)

bubble_sort_time=measure_time(bubble_sort)
selection_sort_time=measure_time(selection_sort)
insertion_sort_time=measure_time(insertion_sort)

print(f'First Bubble sort time: {bubble_sort_time}')
print(f'First Selection sort time: {selection_sort_time}')
print(f'First Insertion sort time: {insertion_sort_time}')

def save_time(file, sort_func):
    with open(file, 'w') as f:
        s=0
        for _ in range(99):
            f.write(str(measure_time(sort_func))+'\n')
            s+=measure_time(sort_func)
        f.write(str(measure_time(sort_func)))
        s+=measure_time(sort_func)
    f.close()
    return s

bubble_sort_times=[save_time('bubble_sort_time.txt', bubble_sort)]
selection_sort_times=[save_time('selection_sort_time.txt', selection_sort)]
insertion_sort_times=[save_time('insertion_sort_time.txt', insertion_sort)]

import statistics
print(f'Average time to sort 100 arrays for the Bubble sort: {statistics.mean(bubble_sort_times)/100}')
print(f'Average time to sort 100 arrays for the Selection sort: {statistics.mean(selection_sort_times)/100}')
print(f'Average time to sort 100 arrays for the Insertion: {statistics.mean(insertion_sort_times)/100}')

import matplotlib.pyplot as plt
with open('bubble_sort_time.txt', 'r') as f:
    bubble_sort_times = [float(t.strip()) for t in f]

with open('selection_sort_time.txt', 'r') as f:
    selection_sort_times = [float(t.strip()) for t in f]

with open('insertion_sort_time.txt', 'r') as f:
    insertion_sort_times = [float(t.strip()) for t in f]

plt.plot(bubble_sort_times, label='Bubble sort')
plt.plot(selection_sort_times, label='Selection sort')
plt.plot(insertion_sort_times, label='Insertion sort')
plt.legend()
plt.xlabel('Board number')
plt.ylabel('Sorting time (s)')
plt.title('Comparison of table sorting times')
plt.show()
