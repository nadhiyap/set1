a=int(input("enter a number"))
l=[]
s=""
for i in range(0,a):
    b=int(input("enter a number"))
    l.append(b)
l.sort()
for e in l:
    s=s+(str(e))
m=len(s)//2
print(s)
print(m)
print(s[m])
