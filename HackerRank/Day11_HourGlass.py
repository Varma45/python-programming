#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
print(arr)
s = [None]*16

def main():
    for i in range(0,16):
        m = int(i/4)
        n = i%4
        print(i)
        for j in range(m,m+3,2):
            temp = 0
            for k in range(n,n+3):
                temp = temp + arr[j][k]
                s[i] = temp + arr[m+1][n+1]
                print(s[i])

        print(max(s))
print(s)
main()