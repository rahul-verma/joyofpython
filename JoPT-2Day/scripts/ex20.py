from jopt.calc import *

calculator = Calculator()

print(calculator.add(3,4))
print(calculator.calc_count)
print(calculator.sub(5,2))
print(calculator.calc_count)
calculator.reset()
print(calculator.calc_count)