#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:49:10 2024

@author: kyleqihua
"""

def gcd(n, d):
    while d % n != 0:
        n, d = d % n, n 
    return n 

# ddb
# It looks like you're on the right track with your implementation! However, there is a small issue with the condition in your while loop. The condition should check if the remainder is not zero, but it should be based on the value of d, not d % n.
# but i still can get the right answer?

# course version
# def gcd(n, d):
#     while d != 0:
#         (d, n) = (n%d, d)
#     return n 
    

print(gcd(8, 12)) # 4
print(gcd(18, 24)) # 6
print(gcd(48, 180)) # 12
print(gcd(101, 103)) # 1