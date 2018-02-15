x=int(input("start="))
y=int(input("end="))
for ii in range(x+1,y):
    s=0
    for i in range(2,ii):
        if(ii%i==0):
             s=1
             break
        else:
            pass
    if(s==0):
        print(ii)
    
    
