# import dependencies
import numpy as np

# create list of all natural numbers below 1000
natural_numbers = np.linspace(0, 999, 1000)

# create empty list that will hold multiples of 3 or 5
multiples = list()

# find the multiples and append them to the list
for x in natural_numbers:
    if (x % 3 == 0 or x % 5 == 0):
        multiples.append(x)
    
# get the sum of the multiples
sum_multiples = sum(multiples)

# print the sum
print(sum_multiples)