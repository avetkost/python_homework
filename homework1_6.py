"""Իրականացնել նախորդ վարժությունում տրված ֆունկցիան՝ հաշվի առնելով, որ առաջին արգումենտը կարող է
մեծ լինել երկրորդից։ Այդ դեպքում ֆունկցիան պետք է վերադարձնի b-ից մինչև a ամբողջ թվերի գումարը։"""

def mijakayq_amb_tveri_gumar (a, b):
    result = 0
    if b >= a:
        counter = a
        limit = b
    else:
        counter = b
        limit = a
    while counter < limit:
        result += counter
        counter += 1
    return result

print(mijakayq_amb_tveri_gumar(2,5))
print(mijakayq_amb_tveri_gumar(5,10))
print(mijakayq_amb_tveri_gumar(55,66))