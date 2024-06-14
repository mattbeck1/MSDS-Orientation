# # import dependencies
# import numpy as np

# def primeNums(n: int) -> list:
#     prime_numbers = list()
#     for i in range(int(n/2), n):
#         if i in [1,2]:
#             prime_numbers.append(i)
#         else:
#             for j in range(2,i):
#                 if (i % j == 0):
#                     break
#             if j == i-1:
#                 prime_numbers.append(i)
#     return prime_numbers

# def main():
#     n = 60085147543
#     p_num = primeNums(n).reverse()
    
#     factors = list()

#     for x in p_num:
#         if n % x == 0:
#             break
    
#     print(x)

# if __name__ == "__main__":
#     main()

import sympy

print(max(sympy.primefactors(600851475143)))
