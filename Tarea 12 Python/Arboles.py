class NodoArbol:
    def __init__(self, value, left= None, rigth= None):
        self.data = value
        self.left = left
        self.right = rigth

print("Arbol 1")
arbol1 = NodoArbol("+", NodoArbol("-", NodoArbol(5), NodoArbol(4)), NodoArbol("*", NodoArbol(3), NodoArbol(2)))
print("\n In Orden")
#5,-,4,+,3,*,2
print(arbol1.left.left.data, end= ",")
print(arbol1.left.data, end= ",")
print(arbol1.left.right.data, end= ",")
print(arbol1.data, end= ",")
print(arbol1.right.left.data, end= ",")
print(arbol1.left.left.data, end= ",")
print(arbol1.right.data, end= ",")
print(arbol1.right.right.data)





print("\n Pre Orden")
#+,-,5,4,*,3,2
print(arbol1.data, end= ",")
print(arbol1.left.data, end= ",")
print(arbol1.left.left.data, end= ",")
print(arbol1.left.right.data, end= ",")
print(arbol1.right.data, end= ",")
print(arbol1.right.left.data, end= ",")
print(arbol1.right.right.data)


print("\n Post Orden")
#5,4,-,3,2,*,+
print(arbol1.left.left.data, end= ",")
print(arbol1.left.right.data, end= ",")
print(arbol1.left.data, end= ",")
print(arbol1.right.left.data, end= ",")
print(arbol1.right.right.data, end= ",")
print(arbol1.data, end= ",")

print("\n ----------------------------")
print("\n Arbol 2")
arbol2 = NodoArbol(40, NodoArbol(30, NodoArbol(25), NodoArbol(35)), NodoArbol(50, NodoArbol(45), NodoArbol(60)))
print("\n In Orden")
#25,30,35,40,45,50,60
print(arbol2.left.left.data, end= ",")
print(arbol2.left.data, end= ",")
print(arbol2.left.right.data, end= ",")
print(arbol2.data, end= ",")
print(arbol2.right.left.data, end= ",")

print(arbol2.right.data, end= ",")
print(arbol2.right.right.data)


print("\n Pre Orden")
#40,30,25,35,50,45,60
print(arbol2.data, end= ",")
print(arbol2.left.data, end= ",")
print(arbol2.left.left.data, end= ",")
print(arbol2.left.right.data, end= ",")
print(arbol2.right.data, end= ",")
print(arbol2.right.left.data, end= ",")
print(arbol2.right.right.data)


print("\n Post Orden")
#25,35,30,45,60,50,40
print(arbol2.left.left.data, end= ",")
print(arbol2.left.right.data, end= ",")
print(arbol2.left.data, end= ",")
print(arbol2.right.left.data, end= ",")
print(arbol2.right.right.data, end= ",")
print(arbol2.data, end= ",")

