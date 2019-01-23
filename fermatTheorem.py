
# Fermat's Theorem

# Reapt until you reach the desired confidence level
# pick a random number n with 1 <= n < p
# calculate n^p-1 mod p
# if the result is not 1, then p is not prime
# if all tests pass, p is probably prime

def isProbablyPrime(n, k = 5):
    if (n < 2 ):
        return False
    output = True
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1):
            return False
    return output