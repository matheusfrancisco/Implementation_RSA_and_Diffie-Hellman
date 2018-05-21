import os
import sys

def modExp(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = modExp(base, exp // 2, mod)
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod

if __name__ == '__main__':
	print('Debug')
	a = modExp(1112232323,200000000000000000000000000000000000000000000012321312312312400000000000000000012,33323)
	print(a)