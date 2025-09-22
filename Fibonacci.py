# Фибоначчи
import math

def f(x):
    cube = abs(x - 2)
    return pow(cube, 3)

def fibonacci_search():
    epsilon = 1e-5
    a = 0.0
    b = 5.0
    count_step = 0
    
    # Вычисляем количество итераций для достижения заданной точности
    n = 0
    F_n_plus_2 = 1
    while F_n_plus_2 < (b - a) / epsilon:
        n += 1
        F_n_plus_2 = fibonacci(n + 2)
    
    # Вычисляем числа Фибоначчи для n итераций
    F_n = fibonacci(n)
    F_n_plus_1 = fibonacci(n + 1)
    F_n_plus_2 = fibonacci(n + 2)
    
    # Начальные точки
    x1 = a + (F_n / F_n_plus_2) * (b - a)
    x2 = a + (F_n_plus_1 / F_n_plus_2) * (b - a)
    
    f1 = f(x1)
    f2 = f(x2)
    count_step += 2
    
    for i in range(n, 0, -1):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fibonacci(i - 1) / fibonacci(i + 1)) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fibonacci(i) / fibonacci(i + 1)) * (b - a)
            f2 = f(x2)
            
        count_step += 1
    
    result = (a + b) / 2.0
    error = (b - a) / 2.0
    
    print(f"Результат: {result}")
    print(f"Погрешность: {error}")
    print(f"Число итераций: {n}")
    print(f"Количество измерений функции: {count_step}")
    print(f"Значение функции: {f(result)}")

def fibonacci(n):
    """Вычисление n-го числа Фибоначчи"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    fibonacci_search()