def binarySort(l, target):
    low = 0
    high = len(l) - 1
    while low <= high:
        middle = (high + low)
        guess = l[middle]
        if guess == target:
            return middle
        if guess > target:
            high = middle - 1
        else:
            low = middle + 1
    return None

l = ["Brian", "Joe", "Lois", "Meg", "Alex", "Peter", "Stewie"]
l = sorted(l)
print(l)
print(binarySort(l, "Lois"))

l2 = [5, 8, 2, 99, 156, 32, 77, 15, 4]
l2 = sorted(l2)
print(l2)
print(binarySort(l2, 15))