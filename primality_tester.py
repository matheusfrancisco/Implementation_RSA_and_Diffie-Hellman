from random import randrange
from modular_arithmetic import *
#Rabin Miller Test to check primality
# Teste de miller rabin

def primality(numero, n_loops=8):
    if numero == 2:
        return True

    if numero < 2 or numero & 1 == 0:
        return False
        
    # numero -1  desloca para direta 1 vez, ou seja divide por 2
    rest = (numero - 1) >> 1
    # print(rest)
    # enquando rest and 1 for  == a zero desloca para direita
    while rest & 1 == 0:
        rest = rest >> 1

    for i in range(n_loops):
        if composto(rest, numero):
            #print('Debug')
            return False
    return True


def composto(rest, numero):
    a = randrange(1, numero)
    if modExp(a, rest, numero) == 1:
        #print('Debug')
        return False
    #r <- 0 to s-1 
    #a^(2^r * d) % n != -1
    exponent = rest
    while exponent < numero - 1:
        if modExp(a, exponent, numero) == numero - 1:
            #print('Debug')
            return False
        exponent = exponent << 1
    return True
if __name__ == '__main__':
    print('Numero primo de 300 digitos')
    numero = primality(250556952327646214427246777488032351712139094643988394726193347352092526616305469220133287929222242315761834129196430398011844978805263868522770723615504744438638381670321613949280530254014602887707960375752016807510602846590492724216092721283154099469988532068424757856392563537802339735359978831013)
    #print(primality(3))
    if(numero==True):
    #print(numero)
        print('Numero é primo')