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
"""

All exercises
        |
        |
        ˅

"""
# 1

# x = float(input("Введите радиус окружности: "))
# print(f"Площадь:{math.pi * x**2} \nДлина:{math.pi * 2 * x}")

# 2

# y = input("Создайте пароль: ")
# time.sleep(5)
# while True:
#     x = input("Введите пароль: ")
#     if x != y:
#         print("Неправильный пароль. Попробуйте еще раз")
#     else:
#         print("""
# ⠄⠄⠄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⢠⣧⠄⣼⠄⠄⠄⠄⠄⠄⠄
# ⣴⣿⡿⣿⣿⣷⠄⠄⠄⠄⠤⠄⢠⣾⣿⣿⣿⣷⣄⠄⠄⠄⠄⠄
# ⢿⡟⠄⠄⣻⡿⠄⠄⠄⠈⠉⠉⢹⣿⣿⣿⣿⣿⡿⠁⠛⠛⠂⠄
# ⠄⠄⠄⢀⡿⠁⠄⠄⠄⠄⠄⠄⢸⣿⡇⠉⠉⠉⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⣼⠁⠄⠄⠄⠄⠄⠄⠄⠄⣿⣷⡀⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⣸⠇⠄⠄⠄⠄⠄⠄⠄⠄⢀⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄⠄
# ⠄⢠⡟⠄⠄⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄
# ⠄⣸⠃⠄⠄⠄⠄⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄
# ⠄⡏⠄⠄⠄⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄
# ⢰⠇⠄⠄⢸⣿⣿⣿⣿⣿⣿⠿⠿⢻⣿⢻⣿⠄⠄⠄⠄⠄⠄⠄
# ⢸⠄⠄⠄⢺⣿⣿⣿⣿⣄⠄⠄⠄⢸⡿⢸⡟⠄⠄⠄⠄⠄⠄⠄
# ⣿⠄⠄⠄⢸⣿⣿⣿⣿⣿⣧⠄⠄⢸⡇⣾⠇⠄⠄⠄⠄⠄⠄⠄
# ⣿⡇⠄⠄⠈⣿⣿⣿⣿⣿⣿⡄⠄⢸⠁⣿⠄⠄⠄⠄⠄⠄⠄⠄
# ⢸⣇⠄⠄⠄⢸⣿⣿⣿⣿⣿⠄⠄⣾⢀⠇⠄⠄⠄⠄⠄⠄⠄⠄
# ⠘⣿⡄⠄⠄⠄⢻⣿⣿⣿⡏⠄⠄⡇⢸⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⢻⣿⡄⠄⠄⠘⣿⣿⡿⠄⠄⢰⡇⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠈⢻⣿⣦⣄⣀⣿⣿⣁⡀⠄⣸⡇⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄
# ⠄⠄⠄⠈⠛⠿⠿⣿⣿⣿⡿⠇⢿⣷⡍⣰⣶⡆⠄⠄⠄⠄⠄⠄
#         """)
#         break
# 3

# x = int(input("Сколько вам лет? "))
# y = (input("Нет ли у вас кредитной задолженности?(y/n) "))
# if x >= 18 and y == "n":
#     print("Кредит был создан успешно :)")
# elif x < 18 and y == "n":
#     print("Вы конечно не имеете кредитов, но это только потому что у вас маленький возраст :(")
# elif x >= 18 and y == "y":
#     print("Вы, бяка, зачем набираете столько кредитов? :((((((")
# 4
# while True:
#     x = int(input("Какой средний балл у ученика? "))
#     if 9 < x <= 12:
#         print("Он отличник")
#         break
#     elif 7 <= x <= 9:
#         print("Он хорошист")
#         break
#     elif 1 <= x < 7:
#         print("Он двоечник")
#         break
#     else:
#         print("Введите еще раз.")
# 5

# y = int(input("Введите 2 действительное число: "))
# x = int(input("Введите 1 действительное число: "))
# if x > y:
#     z = math.sqrt(x * y)
# else:
#     z = math.log(x + y)
# print(z)

# 6

# x = int(input("Temp in room is: "))
# if x > 20:
#     print("On")
# elif x <= 20:
#     print("Off")

# 7

# x = int(input("What number are you? "))
# if x % 2 == 0:
#     print("Второй")
# else:
#     print("Первый")

# 8

# def max(a, b, c):
#     mx = a
#     if b > mx:
#         return b
#     if c > mx:
#         return c
#     else:
#         return mx
#
#
# x = int(input("1 сторона: "))
# y = int(input("2 сторона: "))
# z = int(input("3 сторона: "))
# if x + y > z and z + x > y and z + y > x:
#     print("Это треугольник")
#     if max(x, y, z) ** 2 == y**2 + z**2 or max(x, y, z) == x**2 + z**2 or max(x, y, z) == x**2 + y**2:
#         print("Прямоугольный")
#     elif max(x, y, z) ** 2 > y**2 + z**2 or max(x, y, z) > x**2 + z**2 or max(x, y, z) > x**2 + y**2:
#         print("Тупоугольный")
#     elif max(x, y, z) ** 2 < y**2 + z**2 or max(x, y, z) < x**2 + z**2 or max(x, y, z) < x**2 + y**2:
#         print("Остроугольный")
# else:
#     print("Это не треугольник")

# 9

# x = int(input("x: "))
# y = int(input("y: "))
# if x > 0 and y > 0:
#     print("I")
# elif x > 0 and y < 0:
#     print("IV")
# elif x < 0 and y > 0:
#     print("II")
# elif x < 0 and y < 0:
#     print("III")


# 10

# x = int(input("Enter x: "))
# if x > 0:
#     y = 2 * x - 10
# elif x == 0:
#     y = 0
# elif x < 0:
#     y = 2 * math.fabs(x) - 1
# print(y)
