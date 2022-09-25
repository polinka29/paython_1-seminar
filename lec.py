# Проверить является ли одно число квадратом второго
# a = 5
# b = 25
# if a**2 == b:
#     print('Yes')
# else:
#     print('No')

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if a**2 == b or b**2 == a:
#      print('Yes')
# else:
#     print('No')

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# print (a**2 == b or b**2 == a)

# Найти максимальное число из 5 чисел
# lst = []
# for i in range(5):
#     num = int(input('Введите число: '))
#     lst.append(num)#добавляет в список число
# res = lst[0]
# for i in range(1, 5):
#     if lst[i] > res:
#         res = lst[i]
# print (res)

# # Принимает число N и выводит на печать от минус N до N
# n = int(input('Введите число N: '))
# for i in range(-n, n + 1):
#     print(i, end=' ')#end=' '-выводит результат в строку

# #Принимает число дробь тип float и возвращает первую цифру этой дробной части,после запятой, 1.25=2
# number = float(input('Введите число: '))
# number = int(number*10)%10
# print(number)

# Найти число которое кратно  5 и 10 или 15 но не 30
# n = int(input('Введите число N: '))
# print (n%5 == 0 and n%10 == 0 or n%15 == 0 and n%30 != 0) #and это умножение,or это сложение

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print((not(x or y or z)) == (not x and not y and not z))

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'{x, y, z}:{(not(x or y or z)) == (not x and not y and not z)}')

# Сложить числа вещественного числа
# n = (input('Введите число: '))
# res = 0
# for i in n:
#     if i != '.' and i != ',':
#         res += int(i)
# print(res)

# Проверить является ли строка чисел палиндромом
# n = 'abba'
# count = 0
# for i in range(len(n)//2):
#     if n[i] == n[-1-i]:
#        count += 1
# if count == (len(n)//2):
#     print('palindrom')
# else:
#     print('not palindrom')

# Проверить является ли строка чисел палидромом-решение со срезами
# string = 'abba'
# rev_string = string[::-1] #переворачивает строку
# if rev_string == string:
#    print('palindrom')
# else:
#     print('not palindrom')

# #Написать программу которая выводит из заданого списка нечетные числа и останавливается если встречает число 554
# list = [34, 56, 7, 87, 44, 554]  
# for i in list:
#     if i%2 != 0:
#         print(i, sep = '-')#sep-разделяет знаком в ковычках с новой строки
#     elif i == 554:
#         break

