"""Ստեղծել ֆունկցիա, որը ստանում է երկու թվային արգումենտ` a և b, և վերադարձնում է a-ից մինչև b
ընկած ամբողջ թվերի գումարը։ Կարող եք ենթադրել, որ առաջին արգումենտը միշտ փոքր է երկրորդից։"""

def mijakayq_amb_tveri_gumar (a, b):
    result = 0
    counter = a
    while counter < b:
        result += counter
        counter += 1
    return result

print(mijakayq_amb_tveri_gumar(2,5))
print(mijakayq_amb_tveri_gumar(5,10))
print(mijakayq_amb_tveri_gumar(55,66))