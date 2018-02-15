n=int(input("enter no of values"))
s=int(input("values to sum"))
ll=[]
a=0
for i in range(0,n):
    l=input("enter your list")
    ll.append(l)
for i in range(0,s):
    a+=int(ll[i])
print(a)
