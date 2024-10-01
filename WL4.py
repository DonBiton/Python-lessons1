# #1

# a = input("Введите строку на русском?")
# a = ' ' + a
# print('Кол-во строк начин с е  =', a.count(" е"))
# #2
# a = input("Введите строку на русском?")
# print('Кол-во замен =', a.count(':'), a.replace(':', '%'))
# 3
# a = input("Введите строку на русском?")
# print('Кол-во замен =', a.count('.'), a.replace('.', ''))
# 4
import random
a = [random.randint(-100,100) for x in range(10)]
print(a)
for i in range(len(a)-1):
    if a[i] < 0 and a[i+1] < 0:
        print(a[i], a[i+1])
# 5
a = []
n=input('Введите кол-во элементов в массиве: ')
if not (n.isdigit()):
    print("Вводите число")
    exit()
n=int(n)
for i in range(n):
    b = input('Введите  элемент в массив: ')
    if not (b.isdigit()):
        print("Вводите число")
        exit()
    b=int(b)
    a.append(b)
print(a)
print(b)
min1=10000
for i in range(n-1):
    if b[i]<b[i+1]:
        min1=b[i]
print(min1)