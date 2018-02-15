n=int(input("enter a number"))
s=0
if n in range(1,1000+1):
    num=2
    for i in range(2,n):
        if(n%i==0):
            s=1
            break
if(s==1):
    print("not a prime")
else:
    print("prime")
