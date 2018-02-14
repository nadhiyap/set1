ii=input("enter a number")
i=int(ii)
if i in range(1,100000):
    if(i%2==0):
        print(i,"=even")
    else:
        print(i,"=odd")
else:
    print("enter range between 1 to 100000")
