# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти: '))

if 1:
     print('x > 0 and y > 0')
elif 2:
     print('x < 0 and y > 0')  
elif 3:
     print('x < 0 and y < 0')
elif 4:
     print('x > 0 and y < 0')      
else:
     print('0')  