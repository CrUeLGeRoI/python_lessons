import time


#
#
# def invite(massive):
#     for i in massive:
#         print(f"{i}, приглашаю тебя на обед в ресторане 'All Inclusive'!!! Встреча в 15:30!!! ")
#         time.sleep(0.3)
#
#
# def del_massive(massive):
#     b = 0
#     while massive:
#         del massive[0]
#         b += 1
#     return massive
#
#
# # Task_4
# people = ["Лиза", "Артем", "Настя", "Даня"]
# invite(people)
#
# # Task_5
# time.sleep(2)
# print("От Насти: Я не смогу прийти, у меня куча дел, прости(")
# time.sleep(2)
# people.remove("Настя")  # or people.pop(2)
# people.insert(2, "Арина")
# invite(people)
#
# # Task_6
# print("Я решил купить стол побольше чтобы вместилось еще 3 человека. Я приглашу еще Арину, Дашу и Дарину!")
# people.insert(0, "Арина")
# people.insert(3, "Даша")
# people.append("Дарина")
# invite(people)
# # Task_9
# print(f"Всего я пригласил: {len(people)} человек")
#
#
# # Task_7
# print("Выяснилось, что новый обеденный стол привезти вовремя не успеют и места хватит только для двух гостей.")
#
# i = 0
# while i <= len(people):
#     if len(people) == 2:
#         break
#     x = people[i]
#     people.pop(i)
#     print(f"{x}, я сожалею что так получилось, но я отменяю для тебя приглашение :(")
#
# print(del_massive(people))

# Task_8
# countries = ['USA', 'Canada', 'France', 'Poland', 'Germany']
# print(sorted(countries))
# print(countries)
# print(sorted(countries, reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# Task_10


mountains = ['Everest', 'Kanchenjunga', 'lhotse', 'makalu', 'Kanjut Sar', 'Kamet', 'Himalchuli', 'Broad Peak',
             'Cho Oyu', 'Annapurna I', 'Manaslu', 'Nanga Parbat', 'Distaghil Sar']
print(f"Original for of massive: {mountains}")
print(mountains[2].title())
mountains.pop(1)
print(mountains)
mountains.insert(1, "IT WORKS")
print(mountains)
mountains.reverse()
print(mountains)
mountains.reverse()
mountains.remove('lhotse')
print(mountains)
mountains.append("Append works")
print(mountains)
del mountains[6]
print(mountains)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
mountains.sort(reverse=True)
print(sorted(mountains))
print(len(mountains))
