import math

def f(x):
    cube = abs(x - 2)
    return pow(cube, 3)

def golden_section_search():
    epsilon = 1e-5
    a = 0.0
    b = 5.0
    count_step = 0
    
    # Золотое сечение
    phi = (1 + math.sqrt(5)) / 2
    ratio = 1 / phi
    
    x1 = b - ratio * (b - a)
    x2 = a + ratio * (b - a)
    
    f1 = f(x1)
    f2 = f(x2)
    
    while abs(b - a) > 2 * epsilon:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - ratio * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + ratio * (b - a)
            f2 = f(x2)
            
        count_step += 1
    
    result = (a + b) / 2.0
    error = (b - a) / 2.0
    
    print(f"Результат: {result}")
    print(f"Погрешность: {error}")
    print(f"Число итераций: {count_step}")
    print(f"Значение функции: {f(result)}")

if __name__ == "__main__":
    golden_section_search()