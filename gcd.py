def GCD(a, b):
    while(b != 0):
        remainder = a % b
        print("remainder of {0} mod {1} is {2}".format(a, b, remainder))
        print("a is now {0} and b is now {1}".format(b, remainder))
        GCD(b, remainder)
        a = b
        b = remainder
    return a

print(GCD(78, 66))


def LCD(a, b):
    x = a / GCD(a, b)
    value = x * b
    return value

print(LCD(12, 15))