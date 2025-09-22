# Метод дихотомии
import math

def f(x):
    cube = abs(x - 2)
    return pow(cube, 3)

def main():
    epsilon = 1e-5
    delta = epsilon / 30
    a = 0.0
    b = 5.0
    count_step = 0
    
    while abs(b - a) > 2 * epsilon:
        c = (a + b) / 2.0
        x1 = c - delta
        x2 = c + delta
        
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
            
        count_step += 1
    
    result = (a + b) / 2.0
    error = (b - a) / 2.0
    diff = 2 - result
    
    print("Результат: ", result)
    print("Ошибка: ",error)
    print(f"Число итераций: {count_step}")
    # print(diff)

if __name__ == "__main__":
    main()