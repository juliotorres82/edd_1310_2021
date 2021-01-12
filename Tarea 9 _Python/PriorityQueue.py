class PriorityQueue:
    def __init__( self):
        self.__data = list()

    def is_empty( self):
        return len(self.__data) == 0
    
    def length( self):
        return len(self.__data)
    
    def enqueue(self, prioridad, elem):
        cola = 0
        for x in self.__data:
            if prioridad >= x[0]:
                cola += 1
        if self.is_empty():
            self.__data.append((prioridad,elem))
        else:
            self.__data.insert(cola, (prioridad, elem))

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "|" + str(elem)
        cadena = cadena +"|"
        return cadena
