n=int(input())
sum=0
while(n!=0):
    r=int(n%10)
    # print(n)
    sum=int(int(sum)+int(r))
    # print(sum)
    n=int(n//10)
    # print(n)

print(sum)