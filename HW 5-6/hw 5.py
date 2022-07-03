from typing import Union


class Calculator:
    def add(self, arg_1: Union[int, float], arg_2: Union[int, float]) -> None:
        pass


class IntegerCalculator(Calculator):
    def add(self, arg_1: Union[int, float], arg_2: Union[int, float]) -> int:
        return int(arg_1 + arg_2)


class FloatCalculator(Calculator):
    def add(self, arg_1: Union[int, float], arg_2: Union[int, float]) -> float:
        return float(arg_1 + arg_2)


def make_add(example: Union[IntegerCalculator, FloatCalculator], arg_1: Union[int, float], arg_2: Union[int, float]) -> Union[int, float]:
    return example.add(arg_1, arg_2)


int_calc = IntegerCalculator()
result = make_add(int_calc, 1.0, 2.0)
print(result)  # результат має бути 3
float_calc = FloatCalculator()
result = make_add(float_calc, 1, 2)
print(result)  # результат має бути 3.0
