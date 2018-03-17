a=input("enter a string")
count=0
for i in range(0,len(a)):
    if(a[i].isdigit()):
        count+=1
print("digits=",count)

