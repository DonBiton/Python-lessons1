# 1
a = input('Введите стоимость 1 кг конфет: ')
if not (a.replace('.', '').isdigit()):
    print("Ошибка, вводи числа!")
    exit()
a = float(a)
for i in range(1, 11):
    print('Цена', i, 'КГ', "конфет =", round(i*a, 2))

# 2
b, k = 0, 0
for i in range(1,100_100):
    a=int(input("Введите число:"))
    b = b+a
    k += 1
    if a==0:
        break
print(b,k)

# 3
sm = 0

a = [1, '2', 3, 4, '5', '!', 'FF', '5', '7!']
for i in range(len(a)):
    if str(a[i]).isdigit():
        a[i] = int(a[i])
        sm = sm+a[i]
    else:
        # print('ok')
        for j in range(len(a[i])):
            # print('Вот оно',str(a[i][j]))
            if a[i][j] in '0123456789':
                print(a[i][j])
                sm = sm+int(a[i][j])

print(sm)
