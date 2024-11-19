import numpy as np
from matplotlib import pyplot as plt
a=1
b=1

def f(x):
   return (x**b +a**b)/x**b
plt.grid()
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
x = np.linspace(0, 100, )
plt.plot(x, f(x), color='red')
plt.show()