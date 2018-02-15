n=int(input("enter the number"))
a=n
sum=0
while(n!=0):
    s=n%10
    sum=sum+(s*s*s)
    n=n//10
if(a==sum):
    print("armstrong number")
else:
    print("not armstrong number")
