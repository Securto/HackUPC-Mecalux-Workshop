def count_divisible(start_idx, end_idx, divisor):
    count = 0
    for i in range(start_idx, end_idx):
        if i % divisor == 0:
            count += 1
    return count


import multiprocessing
from concurrent.futures import ThreadPoolExecutor

rangeStart = int(input("Interval start: "))
rangeEnd = int(input("Interval end: "))
num_threads = multiprocessing.cpu_count()
threadRange = int((rangeEnd - rangeStart)/num_threads)

d = int(input("Divisor: "))

executor = ThreadPoolExecutor(max_workers=num_threads)

while( d > 0 ):
    futures = []
    count = 0

    for i in range(num_threads):
        threadStart = rangeStart + threadRange * i
        threadEnd = threadStart + threadRange
        if i == num_threads - 1:
            threadEnd = rangeEnd
        futures.append(executor.submit(count_divisible, threadStart, threadEnd , d))

    for future in futures:
        count += future.result()

    print(count)

    d = int(input("Divisor: "))

