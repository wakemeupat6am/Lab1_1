'''
a = input()
b = input()

if a == b:
    print('Пароли совпадают')
else:
    print('Пароли не совпадают')
'''

'''
n = int(input("Введите номер места:"))
print()
if n % 2 == 0 and n <= 36:
    print ("Верхнее")
elif n % 2 == 0 and n > 36:
    print("Верхнее боковое")
elif n % 2 != 0 and n <= 35:
    print("Нижнее")
else:
    print("Нижнее боковое")
'''

'''
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Весокосный")
else:
    print("Не весокосный")
'''

'''
a = input("первый цвет:")
b = input("второй цвет:")
if a != 'красный' and a !=' желтый 'and a !='синий':
   print('ошибка цвета')
elif b != 'красный'and b !='желтый' and b !='синий':
   print('ошибка цвета')
elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
    print('оранжевый')
elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
    print('зеленый')
elif a =='красный' and b =='красный':
    print('красный')
elif a =='синий' and b =='синий':
    print('синий')
elif a =='желтый' and b =='желтый':
    print('желтый')
'''

'''
n = int(input())
result = []

for i in range(n):
    result.append(input()) # append принимает один аргумент input и добавляет его в конец result

word = ' '.join(result) # join отвечает за объединение списка строк с помощью определенного указателя

print(word)
'''