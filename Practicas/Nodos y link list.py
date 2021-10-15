#Hurray Funciona con listas!!!
class Nodo:
    def __init__(self,data):
        self.data = data
        self.next = None

def nextnode(Nodo1,Nodo2):
    Nodo1.next = Nodo2
    return
def count_nodes(head):
    # assuming that head != None
    n = 1
    current = head
    while current.next is not None:
        current = current.next
        n += 1
    return n
Ix = "y"
a =[]
count = 0
s=(int(input("Ingrese un numero : ")))
a.append(Nodo(s))
head=a[0]
print(head.data)
count += 1 
Ix= str(input("Quieres ingresar otro numero Y/N: "))
while Ix == "y" :
    s=(int(input("Ingrese un numero : ")))
    a.append(Nodo(s))
    nextnode(a[count-1],a[count])
    count += 1 
    Ix= str(input("Quieres ingresar otro numero Y/N: "))
n = count_nodes(head)
print(n)
print("FIn")


#Funciona lo de abajo
"""exec("nodo_" + str(count)+" = Nodo(a)")"""    

"""for x in range(4):
    exec("node" + str(x) + " = 'hello'")
print(node0)
print(node1)
print(node2)
print(node3)
"""

"""head = None
nodoA = Nodo(1)
nodoB = Nodo(3)
nodoC = Nodo(5)
nodoD = Nodo(8)
nodoE = Nodo(10)"""

