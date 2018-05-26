import random
import datetime
from modular_arithmetic import *



random.seed((datetime.datetime.now() 
    - datetime.datetime.utcfromtimestamp(0)).total_seconds())

## Mesmo teste de primalidade do usado no RSA no arquivo primality_tester
def miller_rabin(n, confidence = 40):
    if n == 3:
        return True
    elif n < 3 or n % 2 == 0:
        return False
    
    composite = False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(confidence):
        r = random.randint(2, n - 2)
        x = modExp(r, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for j in range(s - 1):
            x = modExp(x, 2, n)
            if x == 1:
                return False
            elif x == n - 1:
                composite = False
                break
        if composite:
            return False
        composite = False
    return True

def randomNumber(bitLength):
    return random.randint((1 << bitLength - 1) + 1, (1 << bitLength))

def randomLargePrime(bitLength):
    a = 2
    while not miller_rabin(a):
        a = randomNumber(bitLength)
    return a

def EEA(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = EEA(b % a, a)
        return (g, y - (b // a) * x, x)

def multiplicative_inverse(a, n):
    gcd, x, _ = EEA(a, n)
    if gcd == 1:
        return x % n
    else:
        raise ValueError("mult inversa de " + str(a) + " não existe")

def crt(modulo, remainders):
    mod_product = reduce((lambda x, y: x*y), modulo)
    
    total = 0
    for modulus, remainder in zip(modulo, remainders):
        y_i = mod_product // modulus
        z_i = multiplicative_inverse(y_i, modulus)
        total += remainder * y_i * z_i % mod_product
    return total % mod_product


def getGroupWithGenerator(bitLength):

    p = 2
    while not miller_rabin(p):
        q = randomLargePrime(bitLength)
        p = (2 * q) + 1
    
    g = random.randint(2, q)
    while not (pow(g, q, p) and g ** 2 != 1):
        g = random.randint(2, q)
    
    return (p, g)


if __name__ == '__main__':
 	print(miller_rabin(250556952327646214427246777488032351712139094643988394726193347352092526616305469220133287929222242315761834129196430398011844978805263868522770723615504744438638381670321613949280530254014602887707960375752016807510602846590492724216092721283154099469988532068424757856392563537802339735359978831013))