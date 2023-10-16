import re
number_1 = input('Введите элементы ПЕРВОГО списка через: ')
number_1 = re.split(",|;|/", number_1)
number_2 = input('Введите элементы ВТОРОГО списка через: ')
number_2 = re.split(",|;|/", number_2)
number_list_1 = list(number_1)
number_list_2 = list(number_2)
for x in number_list_2:
    if x in number_list_1:
        number_list_1.remove(x)
print(number_list_1)

