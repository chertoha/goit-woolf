import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x ** 2


a, b = 0, 2

N = 10000
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand < f(x_rand)
integral_mc = (b - a) * f(b) * np.sum(under_curve) / N

integral_quad, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {integral_mc}")
print(f"Аналітичний інтеграл (quad): {integral_quad}")
print(f"Абсолютна похибка: {error}")
print(f"Висновок: Quad - точніший")

x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)  # Функція

ax.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', s=1, alpha=0.3)

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Метод Монте-Карло для обчислення інтегралу')
plt.show()
