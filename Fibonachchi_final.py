import math

def f(x):
    cube = abs(x - 2)
    return pow(cube, 3)

def main():
    epsilon = 1e-5
    a = 0.0
    b = 5.0
    
    # Расчет числа вызовов функции для метода золотого сечения
    # Для сравнения, возьмем число вызовов функции из вашего кода,
    # который был 2 + N, где N - количество итераций.
    # В вашем примере: 2 начальных вызова + N итераций = общее_число_вызовов.
    # Если нужно точно такое же число вызовов, то нужно определить N.
    
    # Для метода золотого сечения:
    # 2 начальных вызова. В каждой итерации 1 вызов.
    # Допустим, количество итераций было `count_step_golden`.
    # Тогда общее количество вызовов `count_calls_golden = 2 + count_step_golden`.

    # Для метода Фибоначчи нужно определить количество итераций (N)
    # так, чтобы общее количество вызовов функции было таким же, как в Золотом сечении.
    
    # Определим N_fib так, чтобы 2 + N_fib = count_calls_golden
    # или, если более точно, то N_fib должно быть таким, чтобы
    # (2 + N_fib) было приблизительно равно (2 + count_step_golden).
    # То есть, N_fib ≈ count_step_golden.
    
    # Давайте сначала запустим метод золотого сечения и зафиксируем количество вызовов
    # чтобы потом использовать его для метода Фибоначчи.
    
    # Расчет для золотого сечения (временно, чтобы получить count_calls)
    phi = (math.sqrt(5) - 1) / 2  
    x1_gs = b - phi * (b - a)
    x2_gs = a + phi * (b - a)
    f1_gs = f(x1_gs)
    f2_gs = f(x2_gs)
    count_calls_gs_temp = 2
    count_step_gs_temp = 0
    a_gs_temp = a
    b_gs_temp = b

    while abs(b_gs_temp - a_gs_temp) > 2 * epsilon:
        if f1_gs < f2_gs:
            b_gs_temp = x2_gs
            x2_gs = x1_gs
            f2_gs = f1_gs
            x1_gs = b_gs_temp - phi * (b_gs_temp - a_gs_temp)
            f1_gs = f(x1_gs)
            count_calls_gs_temp += 1
        else:
            a_gs_temp = x1_gs
            x1_gs = x2_gs
            f1_gs = f2_gs
            x2_gs = a_gs_temp + phi * (b_gs_temp - a_gs_temp)
            f2_gs = f(x2_gs)
            count_calls_gs_temp += 1
        count_step_gs_temp += 1
    
    target_calls = count_calls_gs_temp
    
    # Метод Фибоначчи
    # Генерируем числа Фибоначчи
    fib_numbers = [1, 1]
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > (b - a) / epsilon: # Условие для определения N, чтобы охватить интервал
            break
        fib_numbers.append(next_fib)
    
    n_fib = len(fib_numbers) - 1 # N - количество итераций

    # Мы хотим, чтобы количество вызовов функции в Фибоначчи было равно target_calls.
    # В методе Фибоначчи обычно 2 начальных вызова, а затем 1 вызов на итерацию (до последней).
    # В последней итерации может быть 1 или 2 вызова.
    # Если считать 2 вызова на последней итерации, то общее количество вызовов: 2 (начальные) + (N-1) * 1 (по одному на итерацию) + 2 (на последней) = N + 3
    # Но обычно, чтобы соблюсти количество вызовов, мы останавливаемся на N-й итерации, где N - число Фибоначчи.
    # В таком случае, количество вызовов будет N+1 или N+2 в зависимости от реализации последней итерации.
    
    # Давайте используем прямое ограничение по вызовам функции.
    count_step_fib = 0
    count_calls_fib = 0
    
    # Начальные вычисления для Фибоначчи
    # Предполагаем, что N_fib - это количество шагов (итераций)
    # которое нужно для достижения нужной точности, и оно должно
    # быть таким, чтобы общее количество вызовов было target_calls.
    
    # Чтобы иметь такое же количество вычислений,
    # мы должны остановить метод Фибоначчи, когда число вызовов достигнет target_calls.
    # В методе Фибоначчи на каждой итерации делается 1 вызов функции,
    # после двух начальных.
    # Так что, если target_calls = 2 + K, где K - количество итераций после начальных,
    # то мы сделаем K итераций.
    
    # Нужно найти N такое, что F_N >= (b-a)/epsilon
    # N будет количеством интервалов, и N-1 итераций.
    
    # Чтобы количество вызовов было target_calls,
    # мы будем делать target_calls - 2 итераций.
    
    max_iterations = target_calls - 2 # Количество итераций после двух начальных вызовов.
    
    if max_iterations < 0:
        max_iterations = 0

    a_fib = a
    b_fib = b

    # Генерируем числа Фибоначчи до N_max = max_iterations + 2
    fib = [0, 1]
    while len(fib) <= max_iterations + 2:
        fib.append(fib[-1] + fib[-2])
    
    # Проверка на случай, если max_iterations слишком мало
    if max_iterations == 0:
        result = (a_fib + b_fib) / 2.0
        error = (b_fib - a_fib) / 2.0
        print("\nМетод Фибоначчи:")
        print("Результат: ", result)
        print("Ошибка: ", error)
        print(f"Число итераций: {count_step_fib}")
        print(f"Число вызовов функции: {count_calls_fib}")
        return

    # Начальные точки для метода Фибоначчи
    x1_fib = a_fib + (fib[max_iterations] / fib[max_iterations + 2]) * (b_fib - a_fib)
    x2_fib = a_fib + (fib[max_iterations + 1] / fib[max_iterations + 2]) * (b_fib - a_fib)
    
    f1_fib = f(x1_fib)
    f2_fib = f(x2_fib)
    count_calls_fib += 2

    # Итерации метода Фибоначчи
    for k in range(max_iterations, 0, -1): # От N до 1 (включительно)
        if count_calls_fib >= target_calls:
            break
            
        if f1_fib < f2_fib:
            b_fib = x2_fib
            x2_fib = x1_fib
            f2_fib = f1_fib
            if k > 1:
                x1_fib = a_fib + (fib[k-1] / fib[k+1]) * (b_fib - a_fib)
                f1_fib = f(x1_fib)
                count_calls_fib += 1
        else:
            a_fib = x1_fib
            x1_fib = x2_fib
            f1_fib = f2_fib
            if k > 1:
                x2_fib = a_fib + (fib[k] / fib[k+1]) * (b_fib - a_fib)
                f2_fib = f(x2_fib)
                count_calls_fib += 1
        
        count_step_fib += 1
    
    result_fib = (a_fib + b_fib) / 2.0
    error_fib = (b_fib - a_fib) / 2.0

    print("\nМетод Фибоначчи:")
    print("Результат: ", result_fib)
    print("Ошибка: ", error_fib)
    print(f"Число итераций: {count_step_fib}")
    print(f"Число вызовов функции: {count_calls_fib}")

if __name__ == "__main__":
    main()