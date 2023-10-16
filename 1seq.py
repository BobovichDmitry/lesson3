number_item = int(input('Введите количество элементов будущего списка: '))
spisok=[]
print(number_item)
for i in range(number_item):
    spisok.append((input(f"Введите {i+1} элемент списка: ")))
spisok.sort()
print(spisok)