# def num():
#     a = 1
#     for i in range(1, 16):
#         print(a)
# num()

# def describe_pet(animal_type, pet_name):
#     # Выводит информацию о животном.
#     print(f"\nУ меня есть {animal_type}.")
#     print(f"Мой {animal_type} и его зовут {pet_name.title()}.")
#
# describe_pet("хомяк", "гарри")
# describe_pet("собака", "вилли")

def describe_pet(animal_type, pet_name):
    # Выводит информацию о животном.
    r = f"\nУ меня есть {animal_type}."
    r += f"\nМой {animal_type} и его зовут {pet_name.title()}."
    return r


# y = f(x)
s = describe_pet("хомяк", "гарри")
print(s)
