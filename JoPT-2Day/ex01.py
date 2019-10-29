print("The Joy of Python")


def calc_grade(in_expr):
    if in_expr <= 40:
        return "C"
    elif in_expr <= 80:
        return "B"
    else:
        return "A"


print(calc_grade(39))
print(calc_grade(40))
print(calc_grade(41))
print(calc_grade(79))
print(calc_grade(80))
print(calc_grade(81))

print(calc_grade("not_valid"))