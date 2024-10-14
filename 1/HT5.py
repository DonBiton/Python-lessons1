# 1
def find_angle(x, y, z):
    (x1, x2) = x
    (y1, y2) = y
    (z1, z2) = z
    tan_X = x2 / x1 if x1 != 0 else float('inf')
    tan_Y = y2 / y1 if y1 != 0 else float('inf')
    tan_Z = z2 / z1 if z1 != 0 else float('inf')

    if tan_X == tan_Y == tan_Z:
        return X, Y, Z
    if tan_X <= tan_Y and tan_X <= tan_Z:
        if tan_X == tan_Y:
            return X, Y
        elif tan_X == tan_Z:
            return X, Y
        else:
            return X
    elif tan_Y <= tan_X and tan_Y <= tan_Z:
        if tan_X == tan_Z:
            return Y, Z
        else:
            return Y
    else:
        return Z


def input_point(name):
    print(f"Введите координаты точки {name} (формат: x y):")
    x, y = map(str, input().split())
    if not (x.replace('.', '').isdigit()) or not (y.replace('.', '').isdigit()):
        print("Ошибка, вводи числа!")
        exit()
    x, y = float(x), float(y)
    return (x, y)


X = input_point("X")
Y = input_point("Y")
Z = input_point("Z")

print(f"Точка с минимальным углом: {find_angle(X, Y, Z)}")


# 2
def simle(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def bin_palindrom(n):
    bin_palindroms = []
    for i in range(n):
        bin_i = bin(i)[2:]
        if simle(i) and bin_i == bin_i[::-1]:
            s = str(i) + ' = ' + bin_i
            bin_palindroms.append(s)
    return bin_palindroms


n = input('Введите число n: ')
if not (n.isdigit()):
    print('Ошибка, вводи числа')
    exit()
n = int(n)
print(f"Список простых палиндромов в 2 системе: {bin_palindrom(n)}")
