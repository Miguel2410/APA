import numpy as np
import matplotlib.pyplot as plt
import math

log = list(np.arange(0.1,22,1))

x = list(np.arange(0,22,1))

fact = []
for i in x:
   fact.append(math.factorial(i)) #I had to do this because numpy doesn't have the implementation of factorial, and
                                 # the implementation of the function factorial in math.factorial doesn't work with a list, as those functions in numpy do.


plt.plot(x, np.exp(x), label = 'exp')
plt.plot(log, np.log(log), label = 'log')
plt.plot(x, np.sqrt(x), label = 'sqare root')
plt.plot(x, np.exp2(x), label = 'exp2')
plt.plot(x, x, label = 'lineal')
plt.plot(x, fact, label = 'factorial')

plt.xlim(0, 20)
plt.ylim(0, 20)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()