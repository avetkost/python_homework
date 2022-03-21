"""
Իրականացնել pow(a, b) ֆունկցիան՝ հաշվի առնելով, որ b-ն կարող է լինել նաև ոչ դրական։
    Հիշեցնենք`
    a ** b = a ** b, եթե a > 0
    a ** b = (1 / a ** (-b)), եթե b < 0
    a ** b = 1, եթե b = 0
Նաև հաշվի առեք, որ a-ի b աստիճանը սխալ արտահայտություն է, եթե a-ն հավասար է 0, իսկ b-ն բացասական է
"""

def pow (a, b):
    res = 1
    count = 0
    while count < abs(b):
        res *= a
        count += 1
    if b < 0:
        if a == 0:
            return  "0 devision error"
        return  1/res
    return res