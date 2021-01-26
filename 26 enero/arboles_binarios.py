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

        if self.__root == None:
            print("Nada que eliminar")
        else:
            self.__remove(None, None, self.__root, value)

    def __remove(self, padre_hi, padre_hd, actual, value):
        if actual == None:
            print("Caso base")
            return None
        elif actual.data == value: #caso base
            print("Encontrado:", actual.data)
            #caso 1: hoja
            if actual.left == None and actual.right == None:
                if padre_hi != None:
                    padre_hi.left = None
                else:
                    padre_hd.right = None



            #caso 2:con un hijo
            if (actual.left != None and actual.right == None) or (actual.left == None and actual.right != None):
                print("Es un nodo con un hijo", actual.data)
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None


            #caso 3: con los dos hijos
            
            #return actual
        elif value < actual.data:
            print("Buscar a la izquierda")
            self.__remove(actual, None, actual.left, value)
        else:
            print("buscar a la derecha")
            self.__remove(None, actual, actual.right, value)    






















    