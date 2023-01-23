#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# lst = [] 
# lst = list(map(int,input('Enter your number interval: ').split()))
# def my_sum(lst): 
#     sum = 0   
#     for i in range(len(lst)): 
#         if i % 2 != 0: 
#             sum += lst[i] 
#     print(sum) 
# my_sum(lst) 


# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
#разницу между максимальным и минимальным значением дробной части элементов.
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# a = list(map(float,input ("Enter your number: ").split()))
# print(f"Your list is: {a}")
# b = list(map((lambda x: x-(x*10//10)),a))
# print(f'Your difference is: {round(max(b) - min(b), 2)}')

#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# file = input("Enter the program to remove ""абв"" from the text")
# result = list(filter(lambda t: t.find("абв") == -1, file))
# print(result)

#Задана натуральная степень k. Сформировать случайным образом 
#список коэффициентов (значения от 0 до 100) многочлена и записать 
#в файл многочлен степени k. 
# from random import randint 
# max_val = 100
# k = int(input("Enter the natural power k: "))
# koeff = [randint(0,max_val)for i in range(k)]+[randint(1,max_val)]
# poly = "+".join([f'{(j," ")[j == 1]}x^{i}' for i,j in enumerate(koeff) if j][::-1])
# poly = poly.replace("x^1 + ", "x+")
# poly = poly.replace('x^0', '')
# poly = (poly,poly[:-2])[poly[-2:] == '^1']
# print(poly)