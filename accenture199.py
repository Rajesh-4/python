def longestPrefixSuffix(s) : 
    n = len(s) 
      
    for res in range(n // 2, 0, -1) : 
          
        # Check for shorter lengths 
        # of first half. 
        prefix = s[0: res] 
        suffix = s[n - res: n] 
          
        if (prefix == suffix) : 
            return res 
              
  
  
    return 0
      
s = input()
print(longestPrefixSuffix(s))