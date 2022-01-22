car = ['honda', 'mazda', 'lamborghini', 'BMW']
user = ["u1", "u2", "u3", "u4"]
user_V = []


def del_massive(massive):
    b = 0
    while massive:
        del massive[0]
        b += 1
    return massive


# while user:
#     u = user.pop(0)
#     user_V.append(u)
# print(user)
# print(user_V)

print(f"Your garage has:")
for i in car:
    if i == car[-1]:
        print(f"{i}")
    else:
        print(f"{i.title()}")
car.append('Append works!!!')
print(car)

car.insert(1, "AHAHAHAHAHAHA")
car.insert(3, "Breh.")
print(car)

car.pop(1)
print(car)

car.remove("honda")
print(car)

del car[2]
print(car)
print("-" * 20)

del_massive(car)
print(car)
