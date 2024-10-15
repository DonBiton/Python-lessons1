#1
# def f(x):
#     for i in range(len(x)//2):
#         x[i],x[-1-i] = x[-1-i], x[i]
#     return x
# a = []
# m = int(input("Введите длину массива: "))
# for i in range(m):
#     a.append(input('Введите элемент массива: '))
# print(f(a))
#3 
def f(a,b,r,p1, p2 , l1 , l2):
    k=0
    if (p1-a)**2 + (p2 - b)**2 < r**2:
        print("P в окружн")
        k+=1
    if (l1-a)**2 + (l2 - b)**2 < r**2:
        print("L в окружн")
        k+=1
    print(f'всего {k}')
    return ''

a, b , r = input('Введите 2 координаты и r через пробел: ').split()
p1 , p2 = input("точка P ").split()
l1 , l2 = input("точка l ").split()
p1, p2 , l1 , l2 = float(p1),float(p2),float(l1),float(l2)
a,b, r = float(a),float(b),float(r)
print(f(a,b,r,p1, p2 , l1 , l2))


