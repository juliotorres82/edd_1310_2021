class DoubleNode:
    def __init__(self, value, siguiente = None, anterior = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = DoubleNode(None,None,None)
        self.__tail = DoubleNode(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__head == None and self.__tail == None


    def append( self , value ):
        curr_node = NodoDoble( value )
        if self.is_empty() == True:
            self.__head = curr_node
            self.__tail= curr_node
        else:
             curr_node.next = self.__tail
             self.__tail.prev= curr_node
             self.__tail = curr_node 

    def find_from_head(self, value):
        contar = self.__size
        curr_node = self.__head
        while curr_node.next != None and curr_node.data != value:
            curr_node = curr_node.next
            contar+=1
        return contar

    def find_from_tail(self, value ):
        contar = self.__size
        curr_node = self.__tail
        while curr_node.prev != None and curr_node.data != value:
            curr_node = curr_node.prev
            contar+=1
        return contar


    def remove_from_head(self, value):
        curr_node = self.__head 
        if self.__head.data == value:
          self.__head = self.__head.next
        else:
          anterior = None
          while curr_node.data != value and curr_node.next != None: 
            anterior = curr_node
            curr_node= curr_node.next
          if curr_node.data== value:
            anterior.next = curr_node.next
          else:
            print("El dato no existe en la lista")
    
    
    def remove_from_tail(self, value):
        curr_node = self.__tail 
        if self.__tail.data == value:
          self.__tail = self.__head.prev
        else:
          siguiente = None
          while curr_node.data != value and curr_node.prev != None: 
            siguiente = curr_node
            curr_node= curr_node.prev
          if curr_node.data== value:
            siguiente.prev = curr_node.prev
          else:
            print("El dato no existe en la lista")

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.next
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.prev
        print("")
            