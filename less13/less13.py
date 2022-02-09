# 1
# finder_systems = {
#     "Google": 0.9115,
#     "Bing": 0.0423,
#     "Baidu": 0.032,
#     "Yahoo!": 0.0209,
# }
# for a, b in finder_systems.items():
#     print(f"{a} используется в {(b * 100).__round__()}% случаев")

# 2
# today_plans = ['eat', 'drink', 'sleep', 'do python']
# tomorrow_plans = ['eat', 'school', 'drink', 'sleep']
#
# dictionary = {
#     "today": today_plans,
#     "tomorrow": tomorrow_plans
# }
# print(f"Today plans: {dictionary['today']}")
# print(f"Tomorrow plans: {dictionary['tomorrow']}")

# 3
# user = {"u1": "Gleb",
#         "u2": "David",
#         "u3": "Anya",
#         "u4": "Arina"
#         }
# a = str(input("Введите ключ: "))
# if user.get(a):
#     print(f"Hi, {user.get(a)}")
# else:
#     for b in user.values():
#         print(f"Hi, {b}")

# 4
# items = {"Stick": 12,
#          "Oak Log": 32,
#          "Oak Planks": 64,
#          "Apple": 2
#          }
# for a, b in items.items():
#     print(f"{a} — {b}")

# 5
# def createArray(a):
#     createdArray = {}
#     for i in range(1, a + 1):
#         createdArray[i] = i ** 2
#     return createdArray
#
#
# n = int(input("Enter n: "))
# a = createArray(n)
# for b, c in a.items():
#     print(f"Key: {b}\nValue: {c}")
#     print("-" * 20)

# 6
# games = {
#     "3D Shooter": "Tomb Raider",
#     "3D Shooter": "Far Cry",
#     "Fighting": "Mortal Combat",
#     "Stealth-action": "Hitman",
#     "Fighting": "Dead or Alive",
#     "Stealth-action": "Metal Gear Solid"
# }
# print(games)
# for b, c in games.items():
#     print(f"Key: {b}\nValue: {c}")
#     print("-" * 20)
# 7
# a = input("Введите имя и фамилию известного программиста: ")
# proggramers = {
#     "Марк Цукерберг": "14/05/1984",
#     "Ларри Пейдж": "26/03/1973",
#     "Сергей Брин": "21/08/1973"
# }
# for i, j in proggramers.items():
#     if a == i:
#         print(f"Дата рождения {i} — {j}")
# print("Такого программиста нету в мире")

# 8


# 9
def createInfoCity(country, population, fact):
    dictionary = {"country": country, "population": population, "fact": fact}
    return dictionary


city_kharkov = createInfoCity("Ukraine", 1419000, "Рынок Барабашова – самый большой рынок в Европе.")
city_moskva = createInfoCity("Russia", 11920000, "В сердце города хранятся мумифицированные останки В.И. Ленина.")
city_newYork = createInfoCity("New-York", 8200000,
                              "Нью-йоркское метро — самое большое в мире, оно насчитывает более 460 станций. Ежедневно оно перевозит около 8 миллионов пассажиров, что сравнимо с числом жителей этого города.")
city_kyiv = createInfoCity("Ukraine", 2884000,
                           "Самым высоким строением в Киеве остается телебашня, возведенная в 1970-х годах. Установленные на ней передатчики размещены на высоте в 380 метров.")
cities = {
    "Kharkov": city_kharkov,
    "Moskva": city_moskva,
    "New-York": city_newYork,
    "Kyiv": city_kyiv,
}
for i, j in cities.items():
    print("-" * 20)
    print(f"{i}:")
    for a, b in j.items():
        if a == "country":
            print(f"{i} is in country: {b}")
        elif a == "population":
            print(f"The population of {i} is: {b}")
        elif a == "fact":
            print(f"Interesting fact about {i}: {b}")
