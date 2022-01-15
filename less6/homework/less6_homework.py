import time
import sys

# 1

# s = 0  # Start value of sum
# x = 1
# print("S = 1 + 3 + 5 + 7 + 9 +.... + n")
# n = int(input("n: "))
# while True:
#     if n % 2 == 0:
#         print("ВВЕДИТЕ НЕЧЕТНОЕ ЧИСЛО!!!!!")
#         n = int(input("n: "))
#     else:
#         break
# while x <= n:
#     s += x
#     x += 2
# print(f"Sum of {s} value {x - 2}")

# 2
# Cool variant
# a = int(input("Enter num: "))
# if a < 0:
#     a *= -1
# print(f"Length of your number is: {len(str(a))}")
# Mandatory variant
# count = 0
# a = float(input("Enter n: "))
# if a < 0:
#     a *= -1
# while a > 0:
#     a //= 10
#     count += 1
# print(f"Length of your number is: {count}")

# 3
# s = 0  # Start value of sum
# x = 2
# print("S = 1/2 + 1/4 + 1/8 + 1/16 + 1/32 +.... + n")
# n = int(input("n: "))
# while x <= n ** 2:
#     s += 1 / x
#     x *= 2
# print(f"Sum of {float(s)}")
