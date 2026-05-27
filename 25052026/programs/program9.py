import math
a=float(input("Enter co-eff a:"))
b=float(input("Enter co-eff b:"))
c=float(input("Enter co-eff c:"))
discriminant=b**2-4*a*c
if discriminant>0:
    root1=(-b + math.sqrt(discriminant))/(2*a)
    root1=(-b - math.sqrt(discriminant))/(2*a)
    print(f"Root1:{root1}")
    print(f"Root2:{root2}")
elif discriminant==0:
    root=-b/(2*a)
    print(f"Root:{root}")
else:
    real_part=-b/(2*a)
    imaginary=math.sqrt(abs(discriminant))/(2*a)
    print(f"Root1: {real_part} + {imaginary}i")
    print(f"Root2: {real_part} - {imaginary}i")
