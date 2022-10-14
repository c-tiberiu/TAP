# Cautarea liniara

def linearSearch(array, n, x):

    # Parcurgem fiecare element al listei(array)
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = [1, 2, 2, 3, 4, 5, 2]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)