import random
from euclidean import *
from primality_tester import *
from random import randrange, getrandbits


# Função para testar se o numero é primo
# Function to test if a number prime
#
def NumberIsPrime(n):
	if (n==2 or n==3):
		return True
	if (n<2 or n % 3 == 0):
		return False
	return primality(n)



#Function to generete number primes
#Generete two number primes
#Generete nubmer bettew loweNumber UpperNumber
#
def GenereteNumberPrime(n_bits):
	f = False
	while not f:
		# Generate random numbers 
		'''Gera p e q randomicamente n_bits Returns a python long int with k random bits. 
		This method is supplied with the MersenneTwister generator and some other generators
		may also provide it as an optional part of the API.When available, getrandbits() 
		enables randrange() to hsandle arbitrarily large ranges.'''
		p = getrandbits(n_bits)
		#print("Gerando p:",p)
		q = getrandbits(n_bits)
		#print("Gerando q:",q)
		if NumberIsPrime(p) and NumberIsPrime(q) and p!=q:
			f = True

	return p, q


# Função para gerar e and d
# Function compute e and d
# 
def GetParams(phi_n):
	d = 0
	e = 0
	f_e = False

	while f_e == False:
		e = random.randint(1,phi_n-1)
		if (gcd(e,phi_n) == 1):
			f_e = True
	_, d,  _ = euclideanExtendedGCD(e,phi_n)
	
	if(d<0):
		d+= phi_n
	return d, e

def GenParms(n_bits,DEBUG):
	p,q = GenereteNumberPrime(n_bits)
	n = p * q
	#y = carmichael(p, q)
	# totiene
	phi_n= (p-1) *(q-1)
	d, e = GetParams(phi_n)

	#while(d<0):
	#	d+=y

	if DEBUG == True:
		print("P, Q: ", p, q)
		print("N: ", n)
		print("Phi(n): ", phi_n)
		print("E, D: ", e, d)
	return n, d, e 

#Debuger function GenParms
def Gen_Parms2(p,q,DEBUG=True):
	#p,q = GenereteNumberPrime(n_bits)
	n = p * q
	#y = carmichael(p, q)
	# totiente
	phi_n= (p-1) *(q-1)
	d, e = GetParams(phi_n)

	#while(d<0):
	#	d+=y
	
	if DEBUG == True:
		print("P, Q: ", p, q)
		print("N: ", n)
		print("Phi(n): ", phi_n)
		print("E, D: ", e, d)
	return n, d, e 


#Debuge function
if __name__ == '__main__':
	# Testes 
	p = 5023 
	q = 1487
	n,d,e = Gen_Parms2(p,q)


	'''
	Primos Gerados:  5023 1487
	eu to aqui (1, -922031, 384848)
	Chave Publica:  7469201 3114865
	Chave Privada:  6540661
	Mensagem Inicial:  12345
	'''
	'''
	P, Q:  5023 1487
	N:  7469201
	Phi(n):  7462692
	E, D:  0 1
	'''

	#p,q= GenereteNumberPrime(n_bits=3)
	print("Numeros primos")
	print(p,q)


