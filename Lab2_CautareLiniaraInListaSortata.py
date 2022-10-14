list=[]
nr_elemente=int(input("Introduceti numarul de elemente: "))
for i in range(0,nr_elemente):
    element=int(input("Introduceti elementul: "))
    list.append(element)
print(list)

cautare_numar=int(input("Care e nr pe care il cauti?: "))
list.sort()

print("Lista sortata: ", list)

def find_array(list, nr_elemente):
    ok=0
    for i in range(0,nr_elemente):
        if (cautare_numar==list[i]):
            print("In lista sortata, Nr cautat se afla in pozitia ", i+1)
            ok=1
    if (ok==0):
        print("In lista sortata, Nr cautat se afla in pozitia")

find_array(list, nr_elemente)