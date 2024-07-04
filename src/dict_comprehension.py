my_dict = {}

for index, value in enumerate(range(1, 10)):
    my_dict[index] = str(value)

print(my_dict)

my_dict_2 = {index: str(value) for index, value in enumerate(range(1, 10))}

print(my_dict_2)

my_dict_3 = {
    index: str(value) for index, value in enumerate(range(1, 10)) if value % 2 == 0
}

print(my_dict_3)
