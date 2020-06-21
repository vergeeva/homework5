import math


class Signal:
    def __init__(self, a=1, phase=0.5):
        self.__A = a
        self.__phase = phase

    def input_signal(self):
        self.__A = float(input("Введите амплитуду сигнала: "))
        self.__phase = float(input("Введите фазу сигнала: "))

    def __str__(self):
        return f"Амплитуда = {self.__A}, фаза сигнала = {self.__phase}"

    def y(self, x):
        return self.__A * math.sin(x + self.__phase)

    def y_range(self, x0, xn, foot):  # если захочется посчитать с диапазоном
        for i in range(x0, xn, foot):
            print(f"при x = {i}, y = {self.__A * math.sin(i + self.__phase)}")

    # Свойства:
    @property
    def a(self):
        return self.__A

    @a.setter
    def a(self, a):
        self.__A = a

    @property
    def phase(self):
        return self.__phase

    @phase.setter
    def phase(self, phase):
        self.__phase = phase
