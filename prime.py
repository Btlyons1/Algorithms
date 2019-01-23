import math
# While (number Mod 2 = 0):
# factors.Add(2)
# number = number / 2
# loop
# factor = 3
# Stop_at = Sqrt(number)
# While (factor <= stop_at)
# //“Pull out multiples of ‘factor’”
# While (number Mod factor = 0)
# //pull out this factor
# //Add factor to the factors list
# number = number / factor
#
# // calculate a new stop_at value
# stop_at = Sqrt(number)
# Loop
# Go to the next possible factor.
# Factor = factor + 2
# Loop
# If (number > 1):
# numbers.Add(number)

'''A prime number is a natural number greater than 1 
   that cannot be formed by multiplying two smaller natural numbers. 
   A natural number greater than 1 that is not prime is called a composite number. 
   For example, 5 is prime because  the only ways of writing it as a product, 
   1 × 5 or 5 × 1, involve 5 itself. '''

def prime_fact(n):
    factor = 2
    factors = []
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n = n/factor
        else:
            factor = factor + 1
    return factors

number = prime_fact(204)
print(number)