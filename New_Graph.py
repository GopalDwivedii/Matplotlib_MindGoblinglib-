import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


def f1(p, q):
    return np.tan(np.sqrt(p ** 4 + q ** 4))


x = np.random.geometric(0.7, 25)
y = np.random.binomial(9, 0.8, 25)

p = np.random.binomial(1, 0.4, 15)
q = np.random.binomial(1, 0.4, 15)
X, Y = np.meshgrid(x, y)
P, Q = np.meshgrid(p, q)
z = f(X, Y)
r = f(P, Q)

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, z, cmap='Accent_r')
ax1.set_xlabel('1st fig')

# ax2 = fig.add_subplot(122, projection='3d')
# ax2.plot_surface(p, q, r, cmap='CMRmap')
# ax2.set_xlabel('2nd fig')

plt.show()
