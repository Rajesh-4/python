a= int (input())
b=bin(a).replace("0b","")
print(b)
c=0
for i in b:
   
    if(i=='0'):
        c=c+1
print(c)