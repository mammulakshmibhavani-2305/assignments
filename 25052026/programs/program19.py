num=int(input("Enter a number:"))
s=str(num)
d=len(s)
powers=0
temp=num
while temp>0:
    digit=temp%10
    powers+=digit**d
    temp//=10
if powers==num:
    print(f"{num} is an Amstrong number.")
else:
    print(f"{num} is not an Amstrong number.")
