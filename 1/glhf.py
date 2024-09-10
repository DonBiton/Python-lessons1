#a = input('Ваши фамилия, имя? \n ')
#b = input('Сколько Вам лет? \n ')
#c = input('Где вы живете? \n ')
#print('----------------------')
#print('ваше имя фамилия ',a)
#print('Ваш возраст',b)
#print('Вы живете в ' +c)


import math
t = float(input('t = '))
x = float(input('x = '))
x, t=10, 1
z = (9*math.pi*t +10 *math.cos(x))/ (math.sqrt(t) - abs(math.sin(t)))*math.e**x
print(round(z,2))