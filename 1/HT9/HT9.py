import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import *
from matplotlib.gridspec import GridSpec


def f(x, alpha, beta):
    a = alpha
    b = beta
    return (x**b + a**b)/x**b
# 1


fig = plt.figure()
ax = fig.add_subplot()
# Настройки графика
plt.xlabel("x")
plt.ylabel("f(x)")


ax.set_xlim(-20, 20)  # Задаём пределы координат по осям
ax.set_ylim(-15, 15)  # Можно также писать min max
plt.grid()  # Сетка
x_left = np.linspace(-50, - 0.01, 1000)  # Левее точки разрыва
x_right = np.linspace(0.01, 50, 1000)  # Правее точки разрыва
ax.plot(x_left, f(x_left, 1, 1), label=r'$\alpha=1, \beta=1$', color='b')
ax.plot(x_right, f(x_right, 1, 1), color='b')
ax.plot(x_left, f(x_left, 2, 1), label=r'$\alpha=2, \beta=1$', color='r')
ax.plot(x_right, f(x_right, 2, 1), color='r')
ax.plot(x_left, f(x_left, 1, 2), label=r'$\alpha=1, \beta=2$', color='g')
ax.plot(x_right, f(x_right, 1, 2), color='g')
plt.title("Исследование заданной функции - 1")  # название графика
ax.set_xlabel('x', loc='right')  # подпись оси x
ax.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
ax.legend()
plt.savefig('1.svg', dpi=300)
plt.show()


# 2
# Никогда не ставьте plt.title в начало, иначе всем меткам на осях будет очень плохо
# Вместо надо использовать fig.suptitle('Заголовок окна')

fig = plt.figure(dpi=300)
fig.suptitle('Исследование заданной функции - 2')
gs = GridSpec(ncols=8, nrows=8, figure=fig)  # ncols кол-во строк
ax = fig.add_subplot(gs[0:8, 0:8])
# ax = fig.add_subplot()
x = np.linspace(0.01, 50, 1000)
ax.plot(x, f(x, 1, 1), label=r'$\alpha=1, \beta=1$', color='b')
ax.plot(x, f(x, 2, 1), label=r'$\alpha=2, \beta=1$', color='r')
ax.plot(x, f(x, 1, 2), label=r'$\alpha=1, \beta=2$', color='g')
ax.set_xlim(0, 50)  # Задаём пределы координат по осям
ax.set_ylim(-5, 15)  # Можно также писать min max
ax.xaxis.set_major_locator(MultipleLocator(base=5))
ax.yaxis.set_major_locator(MultipleLocator(base=2))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.grid()

ax_min = fig.add_subplot(gs[2:5, 5:7])
x_min = np.linspace(0.0001, 0.01, 10000)
ax_min.plot(x_min, f(x_min, 1, 1), color='b')
ax_min.plot(x_min, f(x_min, 2, 1), color='r')
ax_min.plot(x_min, f(x_min, 1, 2), color='g')
plt.title("Для малых x", fontsize=8)
# ax_min.set_xlim(0,0.01) #Задаём пределы координат по осям
ax_min.set_ylim(0, 10000)  # Можно также писать min max
ax_min.tick_params(axis='x', which='major', labelsize=4)
ax_min.tick_params(axis='y', which='major', labelsize=5)

ax_max = fig.add_subplot(gs[2:5, 2:4])
x_max = np.linspace(10_000, 20_000, 10_000)
ax_max.plot(x_max, f(x_max, 1, 1), color='b')
ax_max.plot(x_max, f(x_max, 2, 1), color='r')
ax_max.plot(x_max, f(x_max, 1, 2), color='g')
plt.title("Для больших x", fontsize=8)
# ax_max.set_xlim(10000,100000) #Задаём пределы координат по осям
ax_max.set_ylim(0, 2)  # Можно также писать max min
ax_max.tick_params(axis='x', which='major', labelsize=4)
ax_max.tick_params(axis='y', which='major', labelsize=5)

ax.set_xlabel('x', loc='right')  # подпись оси x
ax.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
ax.legend()
plt.savefig('2.svg', dpi=300)

plt.show()
# 3
fig = plt.figure(dpi=300)
fig.suptitle('Исследование заданной функции - 3')
gs = GridSpec(ncols=8, nrows=8, figure=fig)  # ncols кол-во строк
ax = fig.add_subplot(gs[0:8, 0:8])
# ax = fig.add_subplot()
x = np.linspace(-50, 0.1, 1000)
ax.plot(x, f(x, 1, 1), label=r'$\alpha=1, \beta=1$', color='b')
ax.plot(x, f(x, 2, 1), label=r'$\alpha=2, \beta=1$', color='r')
ax.plot(x, f(x, 1, 2), label=r'$\alpha=1, \beta=2$', color='g')
ax.plot(x, np.zeros_like(x), label=r'f(x)=0', color='y')
ax.set_xlim(-50, 0)  # Задаём пределы координат по осям
ax.set_ylim(-5, 5)  # Можно также писать min max
ax.xaxis.set_major_locator(MultipleLocator(base=5))
ax.yaxis.set_major_locator(MultipleLocator(base=1))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.grid()

ax_min = fig.add_subplot(gs[4:7, 1:3])
x_min = np.linspace(-1_000_000, -100_000, 10000)
ax_min.plot(x_min, f(x_min, 1, 1), color='b')
ax_min.plot(x_min, f(x_min, 2, 1), color='r')
ax_min.plot(x_min, f(x_min, 1, 2), color='g')
ax_min.plot(x_min, np.zeros_like(x_min), color='y')
plt.title("Для x стремящихся к - бесконечности", fontsize=6)
ax_min.set_xlim(-1_000_000, -100_000)  # Задаём пределы координат по осям
ax_min.set_ylim(-2, 2)  # Можно также писать min max
ax_min.xaxis.set_major_locator(MultipleLocator(base=500_000))
ax_min.yaxis.set_major_locator(MultipleLocator(base=1))
ax_min.tick_params(axis='x', which='major', labelsize=4)
ax_min.tick_params(axis='y', which='major', labelsize=5)
# Убирает 1e6, значаения отображ как надо
ax_min.ticklabel_format(style='plain')
ax.set_xlabel('x', loc='right')  # подпись оси x
ax.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
ax.legend()
plt.savefig('3.svg', dpi=300)
plt.show()


# 4

fig = plt.figure(dpi=300)
fig.suptitle('Исследование заданной функции - 4')
gs = GridSpec(ncols=8, nrows=8, figure=fig)  # ncols кол-во строк
ax = fig.add_subplot(gs[0:8, 0:8])

x_left = np.linspace(-50, - 0.01, 1000)  # Левее точки разрыва
x_right = np.linspace(0.01, 50, 1000)  # Правее точки разрыва
ax.plot(x_left, f(x_left, 1, 0.5), label=r'$\alpha=1, \beta=0.5$', color='b')
ax.plot(x_right, f(x_right, 1, 0.5), color='b')
ax.plot(x_left, f(x_left, 1, -0.5), label=r'$\alpha=1, \beta=-0.5$', color='r')
ax.plot(x_right, f(x_right, 1, -0.5), color='r')
ax.plot(x_left, f(x_left, 1, -1.5), label=r'$\alpha=1, \beta=2$', color='g')
ax.plot(x_right, f(x_right, 1, -1.5), color='g')

plt.grid()  # Сетка
ax.set_xlim(-20, 20)  # Задаём пределы координат по осям
ax.set_ylim(-15, 15)  # Можно также писать min max
ax.set_xlabel('x', loc='right')  # подпись оси x
ax.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
plt.figtext(0.2, 0.4, 'Все графики существуют только при x>0', fontsize=10)
plt.figtext(
    0.2, 0.3, 'Зелёный и красных исходят из 1 точки и возрастают', fontsize=10)
plt.figtext(0.2, 0.2, 'Синий убывает', fontsize=10)
ax.legend()
plt.savefig('4.svg', dpi=300)
plt.show()

# 4.1
fig = plt.figure(dpi=300)
fig.suptitle('Исследование заданной функции - 4')
gs = GridSpec(ncols=19, nrows=8, figure=fig)


x_left = np.linspace(-50, - 0.01, 1000)  # Левее точки разрыва
x_right = np.linspace(0.01, 50, 1000)  # Правее точки разрыва
ax1 = fig.add_subplot(gs[0:8, 0:5])
ax1.plot(x_left, f(x_left, 1, 0),
         label=r'$\alpha=1, \beta=0$', color='b', ls='--')
ax1.plot(x_right, f(x_right, 1, 0), color='b', ls='--')
ax1.plot(x_left, f(x_left, 1, -1),
         label=r'$\alpha=1, \beta=-1$', color='r', ls='--')
ax1.plot(x_right, f(x_right, 1, -1), color='r', ls='--')
ax1.plot(x_left, f(x_left, 1, 0.5), label=r'$\alpha=1, \beta=0.5$', color='g')
ax1.plot(x_right, f(x_right, 1, 0.5), color='g')
ax1.plot(x_left, f(x_left, 1, 0.8), label=r'$\alpha=1, \beta=0.8$', color='y')
ax1.plot(x_right, f(x_right, 1, 0.8), color='y')

plt.grid()  # Сетка
ax1.set_xlim(-15, 15)  # Задаём пределы координат по осям
ax1.set_ylim(-15, 15)  # Можно также писать min max
ax1.set_xlabel('x', loc='right')  # подпись оси x
ax1.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
ax1.legend(fontsize='5')


ax2 = fig.add_subplot(gs[0:8, 6:12])
ax2.plot(x_left, f(x_left, 1, 0),
         label=r'$\alpha=1, \beta=0$', color='b', ls='--')
ax2.plot(x_right, f(x_right, 1, 0), color='b', ls='--')
ax2.plot(x_left, f(x_left, 1, -1),
         label=r'$\alpha=1, \beta=-1$', color='r', ls='--')
ax2.plot(x_right, f(x_right, 1, -1), color='r', ls='--')
ax2.plot(x_left, f(x_left, 1, -0.5),
         label=r'$\alpha=1, \beta=-0.5$', color='g')
ax2.plot(x_right, f(x_right, 1, -0.5), color='g')
ax2.plot(x_left, f(x_left, 1, -0.8),
         label=r'$\alpha=1, \beta=-0.8$', color='y')
ax2.plot(x_right, f(x_right, 1, -0.8), color='y')

plt.grid()  # Сетка
ax2.set_xlim(-15, 15)  # Задаём пределы координат по осям
ax2.set_ylim(-15, 15)  # Можно также писать min max
ax2.set_xlabel('x', loc='right')  # подпись оси x
ax2.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
ax2.legend(fontsize='5')


ax3 = fig.add_subplot(gs[0:8, 13:19])
ax3.plot(x_left, f(x_left, 1, 0),
         label=r'$\alpha=1, \beta=0$', color='b', ls='--')
ax3.plot(x_right, f(x_right, 1, 0), color='b', ls='--')
ax3.plot(x_left, f(x_left, 1, -1),
         label=r'$\alpha=1, \beta=-1$', color='r', ls='--')
ax3.plot(x_right, f(x_right, 1, -1), color='r', ls='--')
ax3.plot(x_left, f(x_left, 1, -1.5),
         label=r'$\alpha=1, \beta=-1.5$', color='g')
ax3.plot(x_right, f(x_right, 1, -1.5), color='g')
ax3.plot(x_left, f(x_left, 1, -2.5),
         label=r'$\alpha=1, \beta=-2.5$', color='y')
ax3.plot(x_right, f(x_right, 1, -2.5), color='y')

plt.grid()  # Сетка
ax3.set_xlim(-15, 15)  # Задаём пределы координат по осям
ax3.set_ylim(-15, 15)  # Можно также писать min max
ax3.set_xlabel('x', loc='right')  # подпись оси x
ax3.set_ylabel('f(x)', loc='top', rotation='horizontal')  # подпись оси y
ax3.legend(fontsize='5')
plt.savefig('4.1.svg', dpi=300)
plt.show()
