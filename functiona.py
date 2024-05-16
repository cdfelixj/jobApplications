from random import randrange
from time import sleep

def process(n, low, high, count=1):
    m = randrange(low, high)
    if m == n:
        print('Bingo !', count)
        return count
    elif m < n:
        count += 1
        new_low = m
        return process(n, new_low, high, count)
    else:
        count += 1
        new_high = m + 1
        return process(n, low, new_high, count)

counts = []
for i in range(20):
    try:
        a = randrange(1, 101)
        c = process(a, 1, 101)
        counts.append(c)
    except Exception as e:
        print(f"An error occurred: {e}")

average = sum(counts) / len(counts)
print("Average number of counts:", average)
