from Seminar2 import print_task as pt
from fractions import Fraction

def menu_task():
    print(pt.print_menu())
    numberdz = int(input('Введите номер задачи: '))
    if numberdz == 1:
        print(pt.print_hex())
        num = int(input('Введите целое число: '))
        print(f'Встроенная функция hex -> \t\t{hex(num)}')
        print(f'Собственная функция self_hex -> \t{self_hex(num)}')
    elif numberdz == 2:
        print(pt.print_fractions())
        first_fract = input('Введите первую дробь формата "a/b": ').split('/')
        second_fract = input('Введите вторую дробь формата "a/b": ').split('/')

        self_fract_1 = SelfFraction(int(first_fract[0]), int(first_fract[1]))
        self_fract_2 = SelfFraction(int(second_fract[0]), int(second_fract[1]))
        original_fract_1 = Fraction(int(first_fract[0]), int(first_fract[1]))
        original_fract_2 = Fraction(int(second_fract[0]), int(second_fract[1]))

        print(f'Свой класс сложения {self_fract_1 + self_fract_2}')
        print(f'Проверка {original_fract_1 + original_fract_2}')

        print(f'Свой класс произведение {self_fract_1 * self_fract_2}')
        print(f'Проверка {original_fract_1 * original_fract_2}')
    else:
        print('Вы ввели неверное число! Повторите ввод!')
        menu_task()


def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result



class SelfFraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise ValueError
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            nod = SelfFraction.check_nod(numerator, denominator)
            self.num = numerator // nod
            self.den = denominator // nod

    def __add__(self, other):
        main_den = self.den * other.den
        main_num = self.num * other.den + other.num * self.den
        return SelfFraction(main_num, main_den)

    def __mul__(self, other):
        main_num = self.num * other.num
        main_den = self.den * other.den
        return SelfFraction(main_num, main_den)

    @staticmethod
    def check_nod(num: int, den: int) -> int:
        nod = 1
        for i in range(1, max(num, den) // 2 + 1):
            if num % i == 0 and den % i == 0:
                nod = i
        return nod

    def __str__(self):
        return f'{self.num}/{self.den}'
