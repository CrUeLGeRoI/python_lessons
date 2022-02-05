# user = {"u1": "human",
#         "u2": "superhero",
#         "u3": "wolf",
#         "u4": "broccoli"
#         }
# print(user)
# print(user["u3"])
# user["u5"] = "Programmer"
# print(user)

# user = {} # создание словаря
#
# user["u1"] = "superhero"
# user["u2"] = "human"
# user["u3"] = "broccoli"
# print(user)
#
# user["u2"] = "wolf"
# print(user)

# a = input("Enter your speed(medium/fastest/else): ")
# info = {"x": 10, "y": 30, "player_speed": a}
# if info["player_speed"] == "medium":
#     x_increment = 2
# elif info["player_speed"] == "fastest":
#     x_increment = 10
# else:
#     x_increment = 1
# info["x"] += x_increment
# print(f"Новая позиция игрока: {info['x']}")

language = {
    "Aleksey": "python",
    "Ilya": "C++",
    "Xlebych": "JS",
    "Vanya": "python bot",
    "Nikiton": "PHP"
}

# for a, b in language.items():
#     print(f"{a} loves {b}")

# for a in language.keys():
#     print(f"{a} loves")

# for a in language.values():
#     print(f"I love {a}")


# info = {
#     'color': 'red',
#     'points': 5
# }
# info1 = {
#     'color': 'green',
#     'points': 15
# }
# info2 = {
#     'color': 'blue',
#     'points': 30
# }
#
# list_of_infos = [info, info1, info2]
# count = 0
# for i in list_of_infos:
#     count += 1
#     print(f"User: {count}")
#     for a, b in info.items():
#         if a == "color":
#             print(f"Color of user: {b}")
#         elif a == "points":
#             print(f"Points: {b}")
# for i in list_of_infos[0:2]:
#     list_of_infos.remove(i)
# print(list_of_infos)

list_huge = []
for i in range(30):
    info = {
        "color": "yellow",
        "points": "15"
    }
    list_huge.append(info)
    print(f"{list_huge}")
for p in list_huge[0:3]:
    if p["color"] == "yellow":
        p["color"] = "blue"
        p["points"] = 100
for x in list_huge:
    print(x)
    print(f"Количество игроков {len(list_huge)}")
for p in list_huge[0:3]:
    if p["color"] == "yellow":
        p["color"] = "blue"
        p["points"] = 100
