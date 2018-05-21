'''
Trabalho de Topicos III
Matheus Francico Batista Machado
Ramon Tramontin
'''
from rsa import RSA
from convertN2T import *


def main():
	print('================== - Criptografia RSA - ======================')

	blockSize = 15

	rsa = RSA()
	msg_f = open("original_msg")
	o_message = msg_f.read()

	print('================== -------------------- ======================')

	numList = str2num(o_message)
	print(' ')
	print('Mensagem original')
	print(o_message)
	print(' ')
	print('---------------------------')
	#print(' ')
	print(numList)
	blocks = num2block(numList, blockSize)
	#print(blocks)
	y = rsa.encryption(blocks)
	print("--------------------------")
	x = rsa.decryption(y)
	numList = block2num(x, blockSize)

	print('---------- Voltando numero para string----------------')
	#print(numList)
	print(' ')
	msg = num2str(numList)
	print(msg)
	
	
	#print('Decrypted message: ', x)




if __name__ == '__main__':
	main()