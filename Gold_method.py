# Метод золотого сечения
import math

def f(x):
    cube = abs(x - 2)
    return pow(cube, 3)

def main():
    epsilon = 1e-5
    a = 0.0
    b = 5.0
    count_step = 0
    count_calls = 0

    # Золотое сечение
    phi = (math.sqrt(5) - 1) / 2  # приблизительно 0.618
    
    # Начальные точки
    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)
    
    f1 = f(x1)
    f2 = f(x2)
    count_calls += 2
    
    while abs(b - a) > 2 * epsilon:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - phi * (b - a)
            f1 = f(x1)
            count_calls += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + phi * (b - a)
            f2 = f(x2)
            count_calls += 1
            
        count_step += 1
    
    result = (a + b) / 2.0
    error = (b - a) / 2.0

    print("Результат: ", result)
    print("Ошибка: ", error)
    print(f"Число итераций: {count_step}")
    print(f"Число вызовов функции: {count_calls}")

if __name__ == "__main__":
    main()