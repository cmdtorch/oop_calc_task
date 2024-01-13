from abc import ABC, abstractmethod
from typing import Callable

from logger import Logger

logger = Logger()


class Calculator(ABC):
    """Абстрактный класс для различных видов калькулятора"""

    @abstractmethod
    def calculate(self, *args: int | float) -> int | float:
        pass


class SimpleCalculator(Calculator):
    """Обычный калькулятор"""

    def __init__(self, operation: Callable):
        self.operation = operation

    @logger.catch  # Захват операции для логирования
    def calculate(self, *args: int | float) -> int | float:
        """Реализация вычисления"""
        if len(args) < 2:
            raise ValueError('Аргументов должно быть два или больше')

        result = args[0]
        for num in args[1:]:
            result = self.operation(result, num)
        return result

    @classmethod
    def new_sum_calculator(cls):
        """Сумма чисел"""
        return cls(lambda a, b: a + b)

    @classmethod
    def new_minus_calculator(cls):
        """Разность чисел"""
        return cls(lambda a, b: a - b)

    @classmethod
    def new_multiplication_calculator(cls):
        """Произведение чисел"""
        return cls(lambda a, b: a * b)

    @classmethod
    def new_exponentiation_calculator(cls):
        """Возведение в степень чисел"""
        return cls(lambda a, b: a ** b)

    @classmethod
    def new_division_calculator(cls):
        """Деление чисел"""
        return cls(lambda a, b: a / b)

    @classmethod
    def new_floor_division_calculator(cls):
        """Целочисленное деление чисел"""
        return cls(lambda a, b: a // b)

    @classmethod
    def new_modulo_operator_calculator(cls):
        """Получение остатка от деления чисел"""
        return cls(lambda a, b: a % b)


if __name__ == '__main__':
    """
    calc = SimpleCalculator.new_sum_calculator() | Создание калькулятора с определенной операцией
    calc.calculate(5, 3)                         | используем для вычисления
    """

    # Сумма
    sum_calc = SimpleCalculator.new_sum_calculator()
    assert sum_calc.calculate(2, 5, 8) == 15

    # Произведение
    multiple_calc = SimpleCalculator.new_multiplication_calculator()
    assert multiple_calc.calculate(3, 3, 2) == 18

    # Возведение в степень
    multiple_calc = SimpleCalculator.new_exponentiation_calculator()
    assert multiple_calc.calculate(5, 2) == 25

    # Получение остатка от деления
    modulo_operator_calc = SimpleCalculator.new_modulo_operator_calculator()
    assert modulo_operator_calc.calculate(9, 2) == 1
