# a= int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a<b and a<c : print(a)
# if b<a and b<c : print(b)
# if c<a and c<a : print(c)
# if a==b or a==c : print('некоторые равны')
a, b, c = input('Введите 3 числа через пробел: ').split()

# if '.' in a or '.' in b or '.' in c:
#     print("Ошибка, вводи целые!")
#     exit ()

if not (a.isdigit()) or not (b.isdigit()) or not (c.isdigit()):
    print("Ошибка, вводи целые!")
    exit()
a, b, c = int(a), int(b), int(c)

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < a:
    print(c)
else:
    print('некоторые равны')

if str(a) in '123':
    print(a)
if str(b) in '123':
    print(b)
if str(c) in '123':
    print(c)
