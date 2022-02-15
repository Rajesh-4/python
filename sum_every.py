# You are given a number N and find the sum of the first N odd and even numbers in a line separated by space. All even and odd numbers should be greater than 0.

# Input:
# First-line will contain the number N.
# Output:
# Print the sum of the first N odd and even numbers in a line separated by space.

# Constraints
# 1≤N≤106
# Sample Input 1:
# 4
# Sample Output 1:
# 16 20
# Sample Input 2:
# 1
# Sample Output 2:
# 1 2

n= int(input())
a= n*2
even=0
odd=0
for i in range (1,a+1):
    if (i % 2==0):
        even=even+i;
    else:
        odd= odd+i;
print (odd,"",even)