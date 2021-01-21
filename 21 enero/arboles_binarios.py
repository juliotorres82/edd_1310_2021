class NodoArbol:
    def __init__(self, value, left= None, right=None):
        self.data = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__ (self ):
        self.__root = None

    def insert(self, value):
        #regla 1
        if self.__root == None:
            self.__root = NodoArbol(value, None, None)

        #regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, no se ingresa nada")
        elif value < nodo.data:
            #regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            #regla 2
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)

    def __recorrido_pos__ (self, nodo):
        if nodo:
            self.__recorrido_pos__(nodo.left)
            self.__recorrido_pos__(nodo.right)
            print(nodo.data, end=", ")

    def __recorrido_pre__ (self, nodo):
        if nodo:
            print(nodo.data, end= ", ")    
            self.__recorrido_pre__(nodo.left)
            self.__recorrido_pos__(nodo.right)

    def __recorrido_in__(self, nodo):
        if nodo != None:
            self.__recorrido_in__(nodo.left)
            print(nodo.data, end=" , ")
            self.__recorrido_in__(nodo.right)

    def transversal(self, format="inorden"):
        if format == "inorden":
            self.__recorrido_in__(self.__root)
        elif format == "preorden":
            print("Recorrido en pre")
            self.__recorrido_pre__(self.__root)
        elif format == "Posorden":
            print("Posorden")
            self.__recorrido_post(self.__root)
        else:
            print("Error, ese formato no existe")

    def search(self, nodo, value):
        if self.__root == None:
            print("vacio")
            return None
        else:

            return self.__search(self.__root, value)
    
    def __search(self, nodo, value):
        if nodo == None: #esta vacio?
            print("Caso base")
            return None
        elif nodo.data == value: #caso base de recursividad
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            print("Buscar a la izquierda")
            
            return self.__search(nodo.left, value)
        else:
            print("buscar a la derecha")
            return self.__search (nodo.right, value)
    
    def remove(self, value):
        encontrado = self.search(value)
        if encontrado.left == None and encontrado.right == None:
            print("Eliminando", encontrado.data)
            encontrado = None
        elif (encontrado.left != None and encontrado.right == None) or \
            (encontrado.left != None and encontrado.right != None):
            print("A eliminar:", encontrado.data)




















    