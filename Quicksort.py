
def partition(array, p, r):
    pivot = array[r]

    # Pointer for greater element
    i = p - 1

    for j in range(p, r):
        if array[j] <= pivot:
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[r]) = (array[r], array[i + 1])
    return i + 1


# Function to perform quicksort
def quick(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick(array, p, q - 1)
        quick(array, q + 1, r)





    