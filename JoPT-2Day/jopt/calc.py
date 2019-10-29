
class Calculator:

    def __init__(self):
        self.__calc_count = 0

    @property
    def calc_count(self):
        return self.__calc_count

    def add(self, a, b):
        self.__calc_count += 1
        return a + b

    # Buggy
    def sub(self, a, b):
        self.__calc_count += 1
        return a * b

    def reset(self):
        self.__calc_count = 0