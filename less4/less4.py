import math
import time

"""

All algebraical systems
            |
            |
            ˅

"""
# B1
# x = int(input("Enter x: "))
# if -math.pi < x < math.pi/4:
#     print(-math.pow(math.cos(x - math.pi), 2))
# elif math.pi/4 <= x <= 1:
#     print(math.sqrt(math.fabs(x + 1)))
# elif 1 < x:
#     print(1 / (x - 1))

# B2
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# if math.fabs(x * y) < 1 and x < 0:
#     print((x + y) / (math.exp(x * y)))
# elif 2 < x and y <= 0:
#     print(-math.pow(math.log(x), 2))
# elif 0 < y and 0 <= x <= 2:
#     print(math.log10(math.sqrt(y)))

# B3
# x = int(input("Enter x: "))
# if 0 <= x < 2:
#     print(x * math.sqrt(math.fabs(x - 5.4)))
# elif 2 <= x < 8:
#     print(math.atan(x ** 2))
# elif 8 <= x:
#     print(math.log10(math.fabs(x - 7.8)))

# B4
# x = int(input("Enter x: "))
# if 1 <= x:
#     print(math.exp(-math.fabs(x)))
# elif math.fabs(x) < 1:
#     print(math.log10(math.sqrt(1 - x**2)))
# elif x <= -1:
#     print(math.atan(x))

# B5
# x = int(input("Enter x: "))
# if 1 < x < 3.2:
#     print(-((1.4 + x) / (math.log(x))))
# elif 0 < x <= 1:
#     print(x**2 - 0.75)
# elif x <= 0:
#     print(math.pow(math.cos(x ** 2), 3) - math.pow(math.sin(x ** 2), 3))

# B6
# x = int(input("Enter x: "))
# if math.fabs(x) < 2:
#     y = x - math.exp(x)
#     print(y)
# elif x <= -2:
#     y = math.log(math.pow(x, 2))
#     print(y)
# elif x >= 2:
#     y = math.pow(math.sin(x), 2)
#     print(y)
