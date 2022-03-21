def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b

"""
Ֆունկցիան վերադարձնում է a թվի գումարը b-թվի մոդուլի հետ, b-ի դրական դեպքում վերադարձնում է a + b
իսկ b-ի բացասական լինելու դեպքում a - b այսինքն a + (-b), որն էլ b-ին դարձնում է դրական։
"""

# Ինչո՞վ է այն տարբերվում հետևյալ սահմանումից

def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    return a - b

"""
Նույն գործողությունն է կատարում հետևյալ ֆունկցիան, բայց  else պայմանը հեռացվել է, 
քանի որ b > 0 դեպքում ֆունկցիան if-ի մեջ կմտներ և դուրս կգար return-ով, իսկ
b <= 0 դեպքում else-ի փոխարեն մեկ է if-ին շարունակող գործողությունն է կատարելու որն էլ նորից նույն
return-ն է ինչ առաջին cod-ում։
"""