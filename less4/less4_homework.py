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
#     if b > a and b > c:
#         return b
#     if c > a and c > b:
#         return c
#     else:
#         return a
#
#
# x = int(input("1 сторона: "))
# y = int(input("2 сторона: "))
# z = int(input("3 сторона: "))
# if x + y > z and z + x > y and z + y > x:
#     print("Это треугольник")
#     if max(x, y, z) ** 2 == y**2 + z**2 or max(x, y, z) ** 2 == x**2 + z**2 or max(x, y, z) ** 2 == x**2 + y**2:
#         print("Прямоугольный")
#     elif max(x, y, z) ** 2 > y**2 + z**2 or max(x, y, z) ** 2 > x**2 + z**2 or max(x, y, z) ** 2 > x**2 + y**2:
#         print("Тупоугольный")
#     elif max(x, y, z) ** 2 < y**2 + z**2 or max(x, y, z) ** 2 < x**2 + z**2 or max(x, y, z) ** 2 < x**2 + y**2:
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
