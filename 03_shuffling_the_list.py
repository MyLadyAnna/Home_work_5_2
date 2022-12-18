# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE
n = int(input('Введите число до какого нужны случайные числа: '))
import random

my_list = []
for i in range(n):
    my_list.append(i)
print(my_list)

for i in range(10):
    rand_index = random.randint(0, len(my_list)-1)    # взяла метод .randint чтобы получить рандомный индекс в пределах последовательности. 
    temp = my_list[i]
    my_list[i] = my_list[rand_index]
    my_list[rand_index] = temp
print('Перемешанный список:')
print(my_list)

