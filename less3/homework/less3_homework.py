# a = int(input("Enter num: "))
# b = int(input("Enter 2nd num: "))
# if a % b == 0:
#     print("Yes")
# else:
#     print("No")
import math

x = int(input("Enter num: "))

if math.fabs(x) < 2:
    y = x - math.exp(x)
    print(y)
elif x <= -2:
    y = math.log(math.pow(x, 2))
    print(y)
elif x >= 2:
    y = math.pow(math.sin(x), 2)
    print(y)
