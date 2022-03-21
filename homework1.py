#homwork1_3
def biggest_sqrt_sum(a, b, c):
    if a > c and b > c:
        return a ** 2 + b ** 2
    elif a > b and c > b:
        return a ** 2 + c ** 2
    else:
        return b ** 2 + c ** 2
#homework1_4
def a_plus_abs_b(a, b):
	if b > 0:
		return a + b
	else:
		return a - b
#

def a_plus_abs_b(a, b):
	if b > 0:
		return a + b
	return a - b


#homework1_7

def pow(a,b):
    res = 1
    count = 0
    while count < abs(b):
        res *= a
        count += 1
    if b < 0:
        if a == 0:
            return "0 division error"
        return  1/res
    return res
