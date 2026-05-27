l=int(input("Enter lower limit of intervals:"))
u=int(input("Enter upper limit of intervals:"))
for n in range(l,u+1):
    order=len(str(n))
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if n==sum:
        print(sum)

