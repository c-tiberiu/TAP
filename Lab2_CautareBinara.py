def search(gramada, piesa):

    for i in range(len(gramada)):
        if (int(gramada[i]) == int(piesa)):
            
            return i
    return -1

def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

number_list = []
piesa = int(input("Element de Cautat: "))
print("\n")
n = int(input("Introdu numarul elementelor: "))
print("\n")
for i in range(0, n):
    print("Introdu' Elementul: ", i, " ")
    item = int(input())
    number_list.append(item)
print("Lista este", number_list)

find = search(number_list, piesa)

if find >= 0:
    print("Am gasit elementul in pozitia: ", find)
else:
    print("Nu am gasit elementul")

number_list.sort()
bSearch = binarySearch(number_list, piesa, 0, len(number_list)-1)

if bSearch < 0:
    print("Cautarea binara nu a gasit elementul")
else:
    print("binary search EVRIKA!!!!")