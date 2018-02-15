i=int(input("enter the number"))
nu=int(input("enter the number"))
sum=0
for i in range(i+1,nu):
    sum=0
    n=i
    while(n!=0):
        s=n%10
        sum=sum+(s*s*s)
        n=n//10
    if(i==sum):
        print(i)
   

    
    
    
    
          
