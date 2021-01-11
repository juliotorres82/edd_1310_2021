from typing import Deque
from Cola import Queue, BounderPriorytyQueue
q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de Queue")
c1={"id":1, "nombre":"Mario", "balance": 20.5}
c2={"id":2, "nombre":"Diana", "balance": 3456.5}
c3={"id":3, "nombre":"Bartolo", "balance": 1000000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido sr. {siguiente['nombre']}, en que podemos servirle el dia de hoy")
print(atencion.to_string())


print("\n --------------------------------------------")
print("Prueba de las colas con prioridad acotada")
print("--------------------------------------------")


maestres = {"prioridad":4, "descripcion":"Maestre", "personas":["juan p", "diego h"]}
niños = {"prioridad":2, "descripcion":"Niños", "personas":["Santi h", "Angel h"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos", "personas":["Diana T", "Maria Z"]}

niñas = {"prioridad":1, "descripcion":"Niños", "personas":["Lupita T", "Karlas C"]}
tercera_edad = {"prioridad":2, "descripcion":"Tercera Edad", "personas":["Ricardo F", "Daniel R"]}
mujeres = {"prioridad":3, "descripcion":"Mujeres", "personas":["Samanta H", "Mariana P"]}
hombres = {"prioridad":3, "descripcion":"Hombres", "personas":["Sebastian E", "Juan M"]}
vigia = {"prioridad":4, "descripcion":"Vigia", "personas":["Alejandro P"]}
timonel = {"prioridad":4, "descripcion":"Timonel", "personas":["Esteban T", "Rodolfo C"]}
capitan = {"prioridad":5, "descripcion":"Capitan", "personas":["Julio M"]}


cpa = BounderPriorytyQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(niñas['prioridad'], niñas)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(tercera_edad['prioridad'], tercera_edad)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)



cpa.to_string()
print("Evacuacion del barco")
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
sig = cpa.dequeue()
print(sig)
cpa.to_string()
