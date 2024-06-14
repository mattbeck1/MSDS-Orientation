# import dependencies
import numpy as np

sequence = [0, 1]


i = 1


even_numbers = list()

while True:
    i += 1
    sum_num = sequence[i-2] + sequence[i-1]
    if sum_num > 4000000:
        break
    sequence.append(sum_num)
    if sum_num % 2 == 0:
        even_numbers.append(sum_num)

print(even_numbers)
print(sum(even_numbers))