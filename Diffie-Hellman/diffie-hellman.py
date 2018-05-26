import os,sys
from modular import *
from modular_arithmetic import *
'''
Cada usuário tem chave pública e privada
Se tu quer enviar uma mensagem pra mim, então eu tenho que fazer alpha^xa
xa é a minha chave privada
alpha é o gerador da classe do numero primo grande que é a chave publica comum
ai eu envio ya = alpha^xa
pra ti
mod p, que é o primo grande
aí tu faz, c1 = alpha^xb mod(p)
xb é a tua chave privada
e c2 = ya^xb * mensagem mod(p)
e envia c1 e c2 pra mim
aí eu recupero a mensagem fazendo k = c1^xa mod(p)
e mensagem = k^-1*c2 mod(p)

'''

class DiffieHellman:
    def __init__(self, prime = None, generator = None):
        self.secret = None
        self.expSecret = None
        self.prime = prime
        self.generator = generator
        self.sharedKey = None
        self.correspondentSecret = None
    
    def generateSecret(self):
        if self.prime == None:
            group = getGroupWithGenerator(256)
            self.prime = group[0]
            self.generator = group[1]
            print(f"Propriedades do grupo \n Primo: {hex(self.prime)}\nGerador: {hex(self.generator)}\n")

        self.secret = random.randint(2, self.prime - 1)
        self.expSecret = modExp(self.generator, self.secret , self.prime)
        print(f"this party sends: {hex(self.expSecret)}")

    def generateSharedKey(self, keyFromOtherEnd = None):
        if keyFromOtherEnd == None:
            keyFromOtherEnd = random.randint(2, self.prime  - 1)
            self.correspondentSecret = keyFromOtherEnd
        
        self.sharedKey = modExp(self.expSecret, keyFromOtherEnd, self.prime)
    
    def verifySharedKey(self):
        if self.correspondentSecret == None or self.sharedKey == None:
            return
        
        correspondentExp = modExp(self.expSecret, self.correspondentSecret, self.prime)
        if self.sharedKey == correspondentExp:
            return True
        return False

dhellman = DiffieHellman()
dhellman.generateSecret()
dhellman.generateSharedKey()
if dhellman.verifySharedKey():
    print(f"Chave compartilhada:\n{hex(dhellman.sharedKey)}")
else:
    print("Erro: os correspondentes NÃO possuem a mesma chave!")
