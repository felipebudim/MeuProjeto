import math
a = float(input("informe o valor de a! "))
b = float(input("informe o valor de b "))
c = float(input("informe o valor de c "))
delta = b * b - 4 * a * c
if delta > (0):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"x1 = {x1:.2f} e x2 = {x2:.2f}")
elif delta == (0):
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"x = {x:.2f}")
else: 
    print("para essa equação não existe valor real para X :(")
                 
