# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:35:14 2023

@author: louis
"""
import sys

#1,2,4,8,16,32
#if 2-4, 4-8, 16-20 are all non decreasing then return YES otherwise return NO

numTests = int(sys.stdin.readline())

res = []

def CheckTest(n,nums):
    if n > 2:
        arr = nums[2:min(4,n)]
 
        for i,j in enumerate(arr[1::]):
            i = int(i)
            j = int(j)
            if j < int(arr[i]):
               
                
                return "NO"
            
                
            
        
    
        if n > 4:
            arr = nums[4:min(8,n)]
           
            for i,j in enumerate(arr[1::]):
                i = int(i)
                j = int(j)
                if j < int(arr[i]):
                    
                    return "NO"
                
        if n > 8:
            arr = nums[8:min(16,n)]
            for i,j in enumerate(arr[1::]):
                i = int(i)
                j = int(j)
                if j < int(arr[i]):
                   
                    return "NO"
                        
                            
    
        if n > 16:
            arr = nums[16:min(20,n)]
            for i,j in enumerate(arr[1::]):
                i = int(i)
                j = int(j)
                if j < int(arr[i]):
                    
                    return "NO"
    return "YES"
            

for i in range(numTests):
    n = int(sys.stdin.readline())
    nums = sys.stdin.readline().rstrip().split(" ")
    res.append(CheckTest(n,nums))

for i in res:
    print(i, file=sys.stdout)
    


    
    
            
            
            
        
    

