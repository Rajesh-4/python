n=int(input())
count=0;
for p in range (1,4):
    for q in range(1,4):
        for r in range (1,4):
         
            if (p*q*r<=n):
                if(p!=q!=r):
                   print(p,q,r)
                   count=count+1;
     
print(count)