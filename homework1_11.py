"""f ֆունկցիան սահմանվում է հետևայլ կերպ.
	f(n) = n, եթե n < 3
	f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3
n-ը կարող է լինել միայն 0 և դրական ամբողջ թիվ։ Իրականացրեք լուծումը ռեկուրսիվ, իտերատիվ և պոչավոր ռեկուրսիվ տարբերակներով։
"""

#Ռեկուրսիա
def func_val_calcul(n):
    if n < 0 or n != int(n): #ստուգում ենք որ դրական ու ամբողջ թիվ լինի
        return "wrong value"
    elif n < 3:              #f(n) = n, եթե n < 3 պայմանի սստուգում
        return n
    else:
        return func_val_calcul(n-1)+func_val_calcul(n-2)+func_val_calcul(n-3)

#print(func_val_calcul(6))

#Պոչավոր Ռեկուրսիա
def func_val_calcul_tail(n, a, b, c):
        if n == 0:
            return a
        return func_val_calcul_tall(n - 1, b, c, a + b + c)

#print(func_val_calcul_tall(6,3,3,5))


#Իտերացիա
def func_val_calcul_iter(n):
    a = 0
    b = 1
    c = 2

    while n > 0:
        n -= 1
        arj = a + b + c
        a = b
        b = c
        c = arj

    return a
#print(func_val_calcul_iter(6))