import os
import sys
import binascii
import math
import random


def str2num(strn):
    '''Conver o caracter para um 
    valor ascii'''
    return [num for num in strn.encode()]

def num2str(msg):
    '''convertendo uma lista de inteiros para uma lista de string'''
    for i in range(len(msg)):
        if msg[i] >= 127:
            msg[i] =127
    return bytes(msg).decode()

def num2block(L, n):
    '''converte uma lista de inteiro
    para locks de tamanho n'''
    splitL = [L[i:i+n] for i in range(0, len(L), n)]   
    if len(splitL[-1]) < n:
        for i in range(n - len(splitL[-1])):    
            splitL[-1].append(0)
    return [int(binascii.hexlify(bytes(blocks)), 16) for blocks in splitL]


def block2num(blocks, n):
    numList = []
    for block in blocks:
        hexnum = hex(block)[2:]
        if len(hexnum) % 2 != 0:
            hexnum = '0' + hexnum 
        numList += [num for num in bytes.fromhex(hexnum)]
    return numList


if __name__ == '__main__':
	print('======================Test================= ')
	blockSize = 15
	msg_f = open("original_msg")
	o_message = msg_f.read()
	print(o_message)
	print('-----------------')
	numList = str2num(o_message)
	print(numList)
	blocks = num2block(numList, blockSize)
	numList = block2num(blocks, blockSize)
	msg = num2str(numList)

	print(msg)
