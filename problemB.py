# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:37:40 2023

@author: louis
"""

import sys

tests = int(sys.stdin.readline())
res = []

for _ in range(tests):
    n,q = sys.stdin.readline().rstrip().split(" ")
    n = int(n)
    q = int(q)
    nums = sys.stdin.readline().rstrip().split(" ")
    queries = sys.stdin.readline().rstrip().split(" ")
    #make hashmap - power of 2 -> list of indicies divisible
    hash_map = {}
    for i,j in enumerate(nums):
        highest = 0
        while int(j) % 2**(highest+1) == 0:
            highest +=1
        for k in range(highest+1):
            if k in hash_map:
                hash_map[k].append(i)
            else:
                hash_map[k] = [i]
        
    
    for query in queries:
        query = int(query)
        if query in hash_map:
            divisibleIndicies = hash_map[query][::]
            
            for i in divisibleIndicies:
              
    
                hash_map[query].remove(i)
                ind = 1
                try:
                    while i in hash_map[query+ind]:
                        hash_map[query+ind].remove(i)
                        ind+=1
                except:
                    pass
                nums[i] = int(nums[i])+ 2**(query-1)
                
                
                
        
    res.append(nums)
for i in res:
    print(str(i).replace("[","").replace(",","")
          .replace("'","").replace("]",""))
        
    
    
        
        
        
        