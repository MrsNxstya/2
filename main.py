import math
from mod import product

def expression(x):
    z = math.exp(math.sqrt(x)) / math.sqrt(1 - x)
    return z

x = float(input("Введіть значення x (0 ≤ x < 1): "))

while x < 0 or x >= 1:
    x = float(input("x має бути в межах [0, 1). Введіть ще раз x: "))

print("Значення виразу z = ", expression(x))

N = int(input("Введіть ціле невід'ємне число N: "))

while N < 0:
    N = int(input("N має бути невід'ємним. Введіть ще раз N: "))

print("Добуток чисел до N = ", product(N))
