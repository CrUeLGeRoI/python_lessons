# # 1
# person = {
#     "first_name": "Artem",
#     "last_name": "Ryabinovich",
#     "age": 15,
#     "city": "Kharkov"
# }
# for i, j in person.items():
#     print(f"{i.title()} : {j}")

# 2
# persons = {
#     "Artem": 13,
#     "Arina": 5,
#     "Liza": 999,
#     "Dasha": 69
# }
# for i, j in persons.items():
#     print(f"{i}`s lucky number is {j}")

# 3 and 4

# termins = {
#     "Список": "набор элементов, следующих в определенном порядке.",
#     "Кортеж": "список, но в котором нельзя изменять или добавлять элементы.",
#     "Логический тип данных": "может принимать одно из двух значений — True (истина) или False (ложь).",
#     "Числа": "могут быть целыми (1 и 2), с плавающей точкой (1.1 и 1.2), дробными (1/2 и 2/3), и даже комплексными.",
#     "Множества": "неупорядоченные наборы значений.",
#     "Словари": "неупорядоченные наборы пар вида ключ-значение.",
#     "Thread (Поток)": "это отдельный поток выполнения.",
#     "Инкапсуляция": "ограничение доступа к составляющим объект компонентам (методам и переменным).",
#     "Наследование": "подразумевает то, что дочерний класс содержит все атрибуты родительского класса, при этом некоторые из них могут быть переопределены или добавлены в дочернем.",
#     "Полиморфизм": "разное поведение одного и того же метода в разных классах."
# }
# for a, b in termins.items():
#     print(f"{a} — {b}")

# 5

# rivers = {
#     "nile": "egypt",
#     "amazon": "south america",
#     "yangtze": "asia",
#     "Mississippi-Missouri": "North America"
# }
# for a, b in rivers.items():
#     print(f"The {a.title()} river is located in {b.title()}")

# 6

# people = {
#     "Artem": True,
#     "Arina": False,
#     "Liza": True,
#     "Dasha": False,
#     "Gleb": True,
#     "Arina": False,
#     "Darina": True,
#     "Danya": True,
#     "Lera": True,
#     "Tania": False,
#     "David": True,
#     "Artem": True
# }
# for a, b in people.items():
#     if b:
#         print(f"{a.title()}, thank you for voting!")
#     else:
#         print(f"{a.title()}, we invite you to vote in the elections of president on 22.02.2022!")

