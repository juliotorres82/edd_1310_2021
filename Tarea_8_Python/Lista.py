class Nodo:
    def __init__( self , value , siguiente= None):
        self.data = value
        self.siguiente = siguiente

class CircularList:
    def __init__( self ):
        self.__head = None
        self.__ref = None
        self.__size = 0

    def is_empty (self):
        return self.__size == 0

    def insert (self, value ):
        if self.is_empty() :
            self.__head = self.__ref= Nodo(value)
            self.__ref.siguiente= self.__head
            self.__size +=1
        elif self.search(value) == True :
              print("No existe")
        elif value > self.__ref.data:
            meruem = self.__ref
            self.__ref = meruem.siguiente= Nodo(value, self.__head)
            self.__size +=1
        elif value < self.__ref.data and value < self.__head.data:
             meruem =  Nodo(value)
             meruem.siguiente = self.__head
             self.__head = meruem
             self.__ref.siguiente = meruem
             self.__size +=1
        elif value < self.__ref.data and  value > self.__head.data:
            meruem = Nodo(value)
            curr_node= self.__head
            while meruem.data > curr_node.siguiente.data:
                curr_node = curr_node.siguiente
            meruem.siguiente= curr_node.siguiente
            curr_node.siguiente= meruem
            self.__size +=1

    def transversal (self):
        curr_node = self.__ref
        while curr_node.siguiente != self.__ref :
            print(f"{ curr_node.siguiente.data } --> " , end="")
            curr_node= curr_node.siguiente
        print(self.__ref.data)

    def search (self, value ):
         meruem = Nodo(value)
         curr_node= self.__ref
         while meruem.data != curr_node.siguiente.data and curr_node.siguiente != self.__ref:
                curr_node = curr_node.siguiente
         if meruem.data == curr_node.siguiente.data :
             return True
         else:
             return False



    def remove( self , value ):
        meruem = Nodo(value)
        curr_node= self.__ref
        if self.search(value) == False :
              print("No existe")
        else:
            while meruem.data != curr_node.siguiente.data and curr_node.siguiente != self.__ref:
                  curr_node = curr_node.siguiente
            if curr_node.siguiente.data == self.__ref.data:
                curr_node.siguiente =  self.__ref.siguiente
                self.__ref = curr_node
                self.__size -=1
            elif curr_node.siguiente.data == self.__head.data:
                self.__head = self.__head.siguiente
                self.__ref.siguiente = self.__head
                self.__size -=1
            elif curr_node.siguiente.data != self.__ref.data and curr_node.siguiente.data != self.__head.data:
                pre = None
                while curr_node.data != value and curr_node.siguiente != self.__ref:
                      pre = curr_node
                      curr_node= curr_node.siguiente
                if curr_node.data == value:
                    pre.siguiente= curr_node.siguiente
                    self.__size -=1