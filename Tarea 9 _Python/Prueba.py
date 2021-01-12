from PriorityQueue import PriorityQueue

pq = PriorityQueue()
print("Comenzando la evacuación: ")
pq.enqueue(4, "Maestre")
pq.enqueue(2, "Niños")
pq.enqueue(4, "Mecánico")
pq.enqueue(3, "Hombres")
pq.enqueue(4, "Vigía")
pq.enqueue(5, "Capitan")
pq.enqueue(4, "Timonel")
pq.enqueue(3, "Mujeres")
pq.enqueue(2, "Tercera edad")
pq.enqueue(1, "Niñas")

while not pq.is_empty():
    pq.to_string()
    print(f"Los siguientes a evacuar son {pq.dequeue()}")
pq.to_string()

print("Ya no queda a nadie por evacuar")


