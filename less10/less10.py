# # Task 1
# names = ["Vanya", "Petya", "Vasya", "Timur", "Gleb", "Tom", "Michael"]
# for i in names:
#     print(i)
#
# # Task 2
# car = ['honda', 'mazda', 'lamborghini']
# for i in car:
#     print(f"Я хочу купить {i.title()}")

# # Task 3
# years_list = [2007, 2008, 2009, 2010, 2011]
# counter = 0
# while counter < len(years_list):
#     if counter == 3:
#         print(f"Мне исполнилось 3 года в: {years_list[counter]}")
#     counter += 1
#
# years_list.append(2012)
# print(years_list)
# most_years = years_list[counter]
# print(f"Больше всего лет мне было в: {most_years}")

# # Task 4
# things = ['wallet', 'mirror', 'umbrella']
# print(things[2].title())
# things[2] = things[2].upper()
# print(things)
# things.pop(2)
# print(things)

# # Task 5
# languages = ['Georgian', 'Estonian', 'Ukrainian']
# languages[2] = languages[2].lower()
# languages.reverse()
# languages[0] = languages[0].title()
# print(languages)

# Task 6
# hardware = ('SSD', 'HDD', 'RAM', 'CPU')
# software = ['Chrome', 'Edge', 'WEB']
# for i in hardware:
#     print(i)
# print('-' * 20)
# for i in software:
#     print(i)
# hardware[1] = "MJPKDDJPKM"
# software[1] = "MJPKDDJPKM"
# print(hardware)
# print(software)
# # В кортежах нельзя изменять элементы

# Task 7
# languages = ['Georgian', 'Estonian', 'Ukrainian', 'French', 'Latvian']
# sorted(languages)
# languages.reverse()
# languages.sort()
# print(languages)

# Task 8
# a = input()
# num_list = []
#
# num = ''
# for char in a:
#     if char.isdigit():
#         num += char
#     elif char == "-":
#         num += char
#     else:
#         if num != '' and num != '-':
#             num_list.append(int(num))
#             num = ''
# if num != '':
#     num_list.append(int(num))
#
# sum = 0
# for i in num_list:
#     sum += i
#
# print(sum)

# Task 9
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

# # Task 10
# list = []
# for i in range(2007, 2022 + 1):
#     list.append(i)
#
# print(list)
