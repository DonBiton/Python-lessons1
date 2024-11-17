import matplotlib.pyplot as plt
import numpy as np
def f(x, alpha, beta):
    a = alpha
    b = beta
    return (x**b)
fig = plt.figure(dpi=200)
plt.title("Исследование заданной функции - 2")
ax = fig.add_subplot()
x = np.linspace(-50,50, 100)
ax.plot(x,f(x,2,2))
ax.grid()

plt.show()