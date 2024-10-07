# 1
a = input("Введите строку: ")
maxn = -1
k = 0
for i in range(len(a)):
    if a[i] == 'н':
        k += 1

        a = a.replace('н', '!', 1)
    else:
        if k > maxn:
            maxn = k
        k = 0
if k > maxn:
    maxn = k
print(a, 'max длина:', maxn)
# 2

a = input("Введите строку с скобкой: ")

for i in range(len(a)):
    if a[i] == '(':
        flag1 = i
    if a[i] == ')':
        flag2 = i
print(a[flag1+1:flag2])

# 3
a = input("Введите строку : ")
a = a.split()
res = [word for word in a if (
    word[0] == 'А' or word[0] == 'а') and word[-1] == 'я']
print(*res)
