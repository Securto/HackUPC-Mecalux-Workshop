def count_divisible(start_idx, end_idx, divisor):
    count = 0

    for i in range(start_idx, end_idx):
        if i % divisor == 0:
            count += 1

    print("There are", count, "numbers divisible by", divisor)


import threading

rangeStart = int(input("Interval start: "))
rangeEnd = int(input("Interval end: "))
d = int(input("Divisor: "))

thread = threading.Thread(target=count_divisible, args=(rangeStart, rangeEnd, d))
thread.start()
thread.join()