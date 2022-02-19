# 1
# def city_country(city, country):
#     return f"{city}, {country}"
#
#
# print(city_country("Ukraine", "Kiev"))
# print(city_country("Russia", "Moskva"))
# print(city_country("USA", "Washington"))
# print(city_country("Poland", "Warshawa"))

# 2
# def make_album(author, album, quantity=None):
#     if quantity is None:
#         dictionary = {author: album}
#     else:
#         dictionary = {author: album, "quantity": quantity}
#
#     return dictionary
#
#
# print(make_album("Dostoyevskiy", "White roses"))
# print(make_album("Dostoyevskiy1", "White roses1"))
# print(make_album("Dostoyevskiy2", "White roses2"))
# print(make_album("Dostoyevskiy3", "White roses3"))
# print(make_album("Dostoyevskiy4", "White roses4", 58))
#
# # 3
# count = 0
# while True:
#     if count > 1:
#         c = input("Вы уже создали больше 1 словаря хотите выйти?(y/n) ")
#         if c == "y":
#             break
#         else:
#             continue
#     a = input("Введите автора: ")
#     b = input("Введите альбом: ")
#     print(make_album(a, b))
#     count += 1
