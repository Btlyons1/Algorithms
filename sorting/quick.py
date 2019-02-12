def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] #recursive case
        less = [i for i in array[1:] if i <= pivot] #sub-array of all elements less than pivot
        greater = [i for i in array[1:] if i >= pivot] #sub-array of all elements greater than pivot
    return quicksort(less) + [pivot] + quicksort(greater)

array = [9, 45, 7, 32, 2, 99, 54]

print(quicksort(array))





