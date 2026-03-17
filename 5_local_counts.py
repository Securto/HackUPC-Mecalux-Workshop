def count_divisible(start_idx, end_idx, divisor):
    global count
    local_count = 0
    for i in range(start_idx, end_idx):
        if i % divisor == 0:
            local_count += 1
    with count_lock:
        count += local_count


import threading

rangeStart = int(input("Interval start: "))
rangeEnd = int(input("Interval end: "))
num_threads = int(input("Number of threads: "))
threadRange = int((rangeEnd - rangeStart)/num_threads)

count = 0
count_lock = threading.Lock()
d = int(input("Divisor: "))

while( d > 0 ):
  threads = []
  count = 0

  for i in range(num_threads):
      threadStart = rangeStart + threadRange * i
      threadEnd = threadStart + threadRange
      if i == num_threads - 1:
          threadEnd = rangeEnd
      threads.append(threading.Thread(target=count_divisible, args=(threadStart, threadEnd , d)))
      threads[-1].start()

  for thread in threads:
      thread.join()

  print(count)

  d = int(input("Divisor: "))

