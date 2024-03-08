"""
13. Напишите функцию, принимающую от 1 до 3 параметров целых
чисел (как стандартная функция range).
    Единственный обязательный аргумент - последнее число.
    Если поданы 2 аргумента, то первый интерпретируется как
начальное число, второй, как конечное (не включительно).
    Если поданы 3 аргумента, то третий аргумент интерпретируется как шаг.
    Функция должна выдавать один из следующих списков: квадратов чисел;
кубов чисел; квадратных корней чисел; логарифмов чисел.
"""

import math
import re


def square(numbers):
    return [x ** 2 for x in numbers]


def cube(numbers):
    return [x ** 3 for x in numbers]


def square_roots(numbers):
    return [round(math.sqrt(x), 2) if x > 0 else 'Недопустимое значение' for x in numbers]


def logarithm(numbers):
    return [round(math.log(x), 2) if x > 0 else 'Недопустимое значение' for x in numbers]


def calculate_option(numbers, choice):
    if choice == 1:
        return square(numbers)
    elif choice == 2:
        return cube(numbers)
    elif choice == 3:
        return square_roots(numbers)
    elif choice == 4:
        return logarithm(numbers)


def enter_values():
    while True:
        input_str = input("\nВводите числа: ")
        numbers = re.findall(r'-?\d+', input_str)

        if len(numbers) != 1 and len(numbers) != 2 and len(numbers) != 3:
            print("Ошибка: некорректный ввод чисел.\n")
            continue

        end = int(numbers[0])
        start = 0
        step = 1

        if len(numbers) == 1:
            if end < 0 or end == 0:
                print("Ошибка: конечное число должно быть больше и не равно нулю")
                continue
        if len(numbers) == 2:
            start = int(numbers[0])
            end = int(numbers[1])
            if end < 0 or end == 0:
                print("Ошибка: конечное число должно быть больше и не равно нулю")
                continue
        elif len(numbers) == 3:
            start = int(numbers[0])
            end = int(numbers[1])
            step = int(numbers[2])
            if step == 0:
                print("Ошибка: шаг должен не может быть равен нулю")
                continue

        if start == end:
            print("Ошибка: пустая последовательность")
            continue

        if start > end and step > 0:
            print("Ошибка: конечное число должно быть больше начального, если шаг положительный (по умолчанию шаг = 1)")
            continue

        if start < end and step < 0:
            print("Ошибка: конечное число должно быть меньше начального, если шаг отрицательный")
            continue

        print("\nКонечное число:", end, "\t\tНачальное число:", start, "\t\tШаг:", step)
        return end, start, step


def calculator(numbers):
    print("Список чисел:", numbers)

    options = {
        1: "Квадраты чисел",
        2: "Кубы чисел",
        3: "Квадратные корни чисел",
        4: "Логарифмы чисел"
    }

    print("\nТип списка:")
    for key, value in options.items():
        print(f"{key}. {value}")

    while True:
        choice = int(input("\nВведите номер выбранного списка или 5 для выхода: "))

        if choice == 5:
            break

        try:
            if 1 <= choice <= 4:
                result = calculate_option(numbers, choice)
                print("\nСписок значений:", result)
            else:
                raise ValueError
        except ValueError:
            print("Ошибка: введен некорректный номер списка.")


def main():
    while True:
        values = enter_values()
        if values:
            end, start, step = values
            numbers = list(range(start, end, step))
            calculator(numbers)
        retry = input("Хотите повторить ввод чисел?\n1) да;\n2) нет.\nВводите: ")
        if retry != "1":
            break


if __name__ == "__main__":
    main()
