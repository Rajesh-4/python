# First and Last Digit Problem Code: FLOW004
# Add problem to Todo list
# Submit
# If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

# Input
# The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the sum of first and last digits of N in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 3 
# 1234
# 124894
# 242323

# Output
# 5
# 5
# 5

n=int(input())

for i in range(0,n):
     num=int(input())
     l=num%10
     while(num>0):
         r=num%10
         num=num//10
     print(l+r)
