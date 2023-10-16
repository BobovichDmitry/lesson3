import re
number = input('Введите элементов будущего списка через запятую: ')
number = re.split(",|;|/", number)
print(number)
res_list=[]
for item in number:
    if item not in res_list:
        res_list.append(item)
    else:
        res_list.remove(item)
print(res_list)