# 2 вариант решения 1 задачи через replace
number = input('Введите число: ')
sum = 0

number = number.replace('.', '')
number = number.replace('-', '')
for item in number:
    sum += int(item)
print(sum)