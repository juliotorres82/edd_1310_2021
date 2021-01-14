from pila import Stack

print("Hacer una funcion que dado un número entero positivo, imprima a la salida una cuenta regresiva hasta cero.")

def regresiva(n):
    if n > 0:
        print(n, end="-" )
        regresiva(n-1)
def main():
    
    valor = 7
    print(f"La cuenta regresiva de {valor} es:")
    regresiva(valor)
main()

print("\n Función recursiva que reciba de entrada una pila con al menos 3 elementos y con recursividad elimine el elemento en la posición media.")
def eliminar_mitad(rev, media, posicion):
  if posicion < media:
        valor = rev.pop()
        eliminar_mitad(rev, media, posicion+1)
        if posicion != media-1:
            rev.push(valor)

def main():

    
    rev = Stack()
    rev.push(1)
    rev.push(2)
    rev.push(3)
    rev.push(4)
    rev.push(5)
    rev.push(6)
    rev.push(7)
    
    eliminar_mitad(rev, round(rev.length()/2), 0)
    
    print("Eliminando la posicion media")
    rev.to_string()
    print(f"La posicion eliminada fue {rev.length()/2+1} al ser el elemento de la posicion media")

    

    

main()
