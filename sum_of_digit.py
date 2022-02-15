# You're given an integer N. Write a program to calculate the sum of all the digits of N.

# Input
# The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, calculate the sum of digits of N, and display it in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 3 
# 12345
# 31203
# 2123
# Output
# 15
# 9
# 8

n=int(input())
arr=[]

for i in range (0,n):
    arr.append(int(input()))

for i in range(0,n):
    sum=0
    while(arr[i]!=0):
         r=int(arr[i]%10)
    # print(n)
         sum=int(int(sum)+int(r))
    # print(sum)
         arr[i]=int(arr[i]//10)
    # print(n)

    print(sum)