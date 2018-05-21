#!/usr/bin/python
import os ,sys
from rsa import *
from convertN2T import *

'''
	Message Digest - MD 
		- Garantindo assinatura digital tem que verificar as seguintes propriedades

			* Um usúario não pode forjar a assinatura de outro usuário e as assinaturas 
				digitais devem ser únicas para cada usúario

			* O emissor de uma mensagem não pode invalidar a assinatura de uma mensagem.
				Ou seja, não pode negar o envio de uma mensagem com sua assinatura;

			* O receptor da mensagem não pode modificar a assinatura contida na mensagem;

			* Um usuário não pode ser capaz de retirar a assinatura de uma mensagem e
				colocar em outra	
			

			Para que o metodo rsa fique ainda mais seguro, a mensagem pode ser assinada. Suponha
			que uma mensagem codificada será enviada de a para b, e que ambos tenham uma
			chave publica C e sua respctiva chave privada D.
			Quando a for enviar a mensagem então ao invés de enviar Cb(m), ele envia Da(Cb(m)).
			Logo quando b receber a mensagem codificada, para decodificar-la ele usa a sua chave
			privada e a chave publica de b, assim Db(Ca(Da(Cb(m)))) ≡ Db(Cb(m)) ≡ m. Se a
			mensagem final fizer sentido, então b terá certeza que essa mensagem veio de a. 

'''


def encryption_(msg,d,n):
	res = []
	for i in msg:
		res.append(modExp(i,d,n))

			
	print(' \n')
	print('Mensagem criptografada:', res)
	return res

def assinatura(msg, e ,	n):
    res = []
    for i in msg:
    			res.append(modExp(i,e,n))
    #print('Mensagem assinada:', res)
    return res

def decryption_verify(msg,na,ea,nb,db):
	res = []
	for i in msg:
		res.append(modExp(i,ea,na))

	res_1 = []
	for i in msg:
		res_1.append(modExp(i,db,nb))
	#print('Mensagem Decriptografada :',res_1)
	return res_1 #res

def verefy(msg,msg_original):
	print("mensagem assinada que você recebeu\n\n")
	print(msg)
	print("\n")
	print("mensagem original que foi enviada\n\n")
	print(msg_original)
	print("\n")

if __name__ == '__main__':
	blockSize = 15
	rsa_b = RSA()
	rsa_a = RSA()

	#Bob quer enviar uma msg e verificar ela
	msg_f = open("original_msg")
	msg_f = msg_f.read()
	#convertando para ascii
	numList = str2num(msg_f)
	blocks = num2block(numList, blockSize)

	#Chaves de Bob
	(Nb, Eb) = rsa_b.publicKey()
	(Nb, Db) = rsa_b.privateKey()
	
	#Chaves de Alice
	(Na, Ea) = rsa_a.publicKey()
	(Na, Da) = rsa_a.privateKey()
	
	#alice encripta a msg com a chave privada dela
	#alice, (Na,Da)(Nb,Eb(m)) e assina com 
	#alice assina a msg com a chave publica de bob
	y_assinada = assinatura(blocks,Eb,Nb)
	# dps criptografa com sua privada
	y = encryption_(y_assinada,Da,Na)

	
	

	#bob tem a chave publica de alice, e tem a sua propria chave privada
	#bob aplica (Nb,Db){(Na,Ca)[((Na,Da)((Nb,Eb)(m)))]}
	x_verifica_assinatura =  decryption_verify(y_assinada,Na, Ea,Nb,Db)
	numList = block2num(x_verifica_assinatura, blockSize)
	msg = num2str(numList)

	verefy(msg,msg_f)




	