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
def func_val_calcul_tall(n,acc):
    if n < 0 or n != int(n): #ստուգում ենք որ դրական ու ամբողջ թիվ լինի
        return "wrong value"
    elif n < 3:
        return n             #f(n) = n, եթե n < 3 պայմանի սստուգում
    else:
        return func_val_calcul(n-1*acc)

print(func_val_calcul_tall(6,3))


#Իտերացիա