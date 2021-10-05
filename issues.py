# 1

city_arr = ['Москва', 'Санкт-Петербург', 'Воронеж', 'Томск', 'Новосибирск', 'Тверь']


def splitting(arr):
    splitted_arr = " ,".join(arr)
    return f'{splitted_arr}.'


print(splitting(city_arr))

# 2
import random
num = random.uniform(0, 100)  # случайное число для инициализации


def round5(number):
    if number % 5 >= 2.5:  # если остаток от деление числа на 5 больше или равен 2,5
        number = 5 * (number // 5 + 1)  # то number = 5*(целое число пятерок в числе + 1) - округление вверх
    else:
        number = 5 * (number // 5)      # иначе number = 5*(целое число пятерок в числе) - округление вниз
    return number


print(f'{num} => {round5(num)}')

# 3
num = random.randint(0, 150)  # число для инициализации


def cases(number):
    last_num = number % 10
    if number % 100 == 11:  # для чисел, оканчивающихся на 11
        skl = 'ов'
    elif last_num == 1:
        skl = ''
    elif 2 <= last_num <= 4:
        skl = 'а'
    else:
        skl = 'ов'
    return f'{number} компьютер{skl}'


print(cases(num))

# 4
num = 113


def is_simple(number):
    status = 0
    if number == 2:
        status = True  # 2 - простое число и минимальный делитель
    elif number <= 1:  # если меньше 1, то точно не простое
        status = False
    else:              # для всех других чисел проверяются делители
        for i in range(2, number-1):
            if number % i == 0:  # если делится без остатка на делители, то уже не простое
                status = False
                return status
        status = True  # если проверил все делители и ни один не подошел, значит простое число
    return status


if is_simple(num):
    print(f'Число {num} является простым')
else:
    print(f'Число {num} не является простым')


# 5
arr1 = [7, 17, 1, 9, 1, 17, 56, 56, 23]
arr2 = [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]


def repeated_nums(array1, array2):
    buf_arr = list()
    for i in array1:
        count_i1 = array1.count(i)  # подсчет количества одинаковых элементов в 1 массиве
        count_i2 = array2.count(i)  # подсчет количества одинаковых элементов во 2 массиве
        if count_i1 >= 2 and count_i2 >= 2:  # если в обоих массивах одного и того же числа больше 2х, то добавляется в новый массив
            buf_arr.append(i)
    buf_set = set(buf_arr)  # Преобразование во множество, чтобы оставить только уникальные элементы
    buf_arr = sorted(list(buf_set))  # превращение в массив (список Python) и его сортировка (необязательно)
    return buf_arr


print(repeated_nums(arr1, arr2))
