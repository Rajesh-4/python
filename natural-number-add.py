# You are given a number N. Find the sum of all numbers from 1 to N.

# Input:
# First-line will contain the number N.
# Output:
# Print the answer in a single line.

# Constraints
# 1≤N≤109
# Sample Input 1:
# 4
# Sample Output 1:
# 10
# Sample Input 2:
# 8
# Sample Output 2:
# 36
# EXPLANATION:
# In the first example, (1 + 2 + 3 + 4) = 10.
# In the second example, (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) = 36.

n=int(input())
s=int(n*(n+1))
s=s//2
print(s)

