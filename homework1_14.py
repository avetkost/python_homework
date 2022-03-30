def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def halve(n):
    return n / 2

# Ռեկուրսիվ լուծում
def fast_mul_rec(a, b):
    if b == 0:
        return 0
    if is_even(b):
        return double(fast_mul_rec(a, halve(b)))
    return a + (fast_mul_rec(a, b - 1))

# Իտերատիվ լուծում
def fast_mul_iter(a, b):
    res = 0
    while b > 0:
        if not is_even(b):
            res += a
            b -= 1
        a = double(a)
        b = halve(b)
    return res