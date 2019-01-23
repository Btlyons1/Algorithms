

# Init an array is-prime
# Corss out multiples of 2
# for p = 3 to sqrt(n) step 2
# make sure p is prime
# if (is_prime[p]) then
# cross out multiples of p.
# for multiple = p * p to N step 2 * p
# is_prime[multiple] = False
# next multiple
# end if
# next p

# Python program to print all primes smaller than or equal to n

def sieveOfEratosthenes(n):
    is_prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * 2, n+1, p):
                is_prime[i] = False
        p += 1

    for p in range(2, n):
        if is_prime[p]:
            print(p)


sieveOfEratosthenes(30)