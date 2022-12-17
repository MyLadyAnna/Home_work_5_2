# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его
# на экран, а так же сумму элементов списка.

number = int(input('Введите количество чисел в последовательности: '))
my_list = []
sum = 0

for i in range(1,number+1):    
    num = round((1 + 1/i)**i,2)
    my_list.append(num)
    sum += num
print(my_list)
print(f'Сумма чисел в последовательности: {sum}')
