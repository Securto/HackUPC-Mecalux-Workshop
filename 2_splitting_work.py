def count_divisible(start_idx, end_idx, divisor):
    count = 0

    for i in range(start_idx, end_idx):
        if i % divisor == 0:
            count += 1

    print("There are", count, "numbers divisible by", divisor)


import threading

rangeStart = int(input("Interval start: "))
rangeEnd = int(input("Interval end: "))
num_threads = int(input("Number of threads: "))
threadRange = int((rangeEnd - rangeStart)/num_threads)

d = int(input("Divisor: "))

while( d > 0 ):
  for i in range(num_threads):
      threadStart = rangeStart + threadRange * i
      threadEnd = threadStart + threadRange
      if i == num_threads - 1:
          threadEnd = rangeEnd
      thread = threading.Thread(target=count_divisible, args=(threadStart, threadEnd , d))
      thread.start()
  d = int(input("Divisor: "))

