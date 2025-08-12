'''
https://leetcode.ca/all/254.html

254. Factor Combinations

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.
'''
from math import sqrt

def find_factors(num):
    res = []

    def backtrack(n, start, path):
        if n == 1:
            if len(path) > 1:
                res.append(path)
            
            return 
        
        for f in range(start, int(sqrt(n))):
            if n % f == 0:
                path.append(f)
                backtrack(n//f, f, path)
                path.pop()
        
        if n >= start:
            path.append(n)
            backtrack(1, n, path)
            path.pop()
      
    backtrack(num, 2, [])
    return res