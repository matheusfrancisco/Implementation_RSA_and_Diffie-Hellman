import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
# Caso queira mudar o tamanho dos números primos "não exagere" alterar n_bit em RSA GenParms

class RSA(object):

	n =0
	d =0
	e =0

	def __init__(self):
		self.n, self.d, self.e = GenParms(n_bits=100, DEBUG=True)

	def encryption(self, msg):
		#print('Mensagem original:', msg)
		
		# rest congrunte m^e (mod n) 
		#res = modExp(msg, self.e, self.n)
		res = []
		for i in msg:
			res.append(modExp(i,self.e,self.n))

		
		print(' \n')
		print('Mensagem criptografada:', res)
		return res

	def decryption(self, msg):
		#res = pow(msg,self.d,self.n)
		# c^d congruente (m^e)^d congruente m(mod n) 
		#
		#print('Mensagem criptografada :',msg)
		res = []
		for i in msg:
			res.append(modExp(i,self.d,self.n))
		#res = pow(msg, self.d , self.n)
		print('Mensagem Decriptografada :',res)
		return res #res
	
	def publicKey(self):
		return(self.n,self.e)

	def privateKey(self):
		return(self.n,self.d)


if __name__ == '__main__':
	print("Rotina de testes:")
	rsa = RSA()
	

	print('')