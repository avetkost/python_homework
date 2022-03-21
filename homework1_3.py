#homwork1_3
def biggest_sqrt_sum(a, b, c):
    if a > c and b > c:
        return a ** 2 + b ** 2
    elif a > b and c > b:
        return a ** 2 + c ** 2
    else:
        return b ** 2 + c ** 2

