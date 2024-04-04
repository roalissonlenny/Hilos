from lib import *
import threading
import time

"""
def timeMaker():
    print("Haciendo tiempo...")
    time.sleep(2) #segundos
    print("Tiempo hecho...")


timeMaker()

listaHilos =[]
for i in range(4):
    t = threading.Thread(target=timeMaker)
    listaHilos.apped( t )
    t.start()

for t in listaHilos:
    t.join()
tf = time.time() - t0

print(f'Tiempo total de ejecucion: {tf}')
"""

"""
print("hilo principal o 1 hilo")
print()
def contador (inicio, fin):
    arrayNum = []
    for i in range (inicio, fin+1, 1):
        arrayNum.append(i)
        time.sleep(0.01)
    return arrayNum

t0 = time.time()
listaNumeros = contador(1,100)
tf = time.time() - t0
print(f'Tiempo de ejecucion: {tf}')
print(listaNumeros)
print("----------------------------")

print("Usando 2 hilos")
print()

globalArrayNum = []
def contador2 ( inicio, fin ):
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0


t0 = time.time()
listaHilos = []
t = threading.Thread(target=contador2, args=(1,50))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contador2, args=(51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()

tf= time.time() - t0

print(f'Tiempo de ejecucion: {tf}')
print(globalArrayNum)
print("-----------------------------")
"""

"""
print("Usando 4 hilos")
print()

globalArrayNum = []
def contador3 ( inicio, fin ):
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0 = time.time()
listaHilos = []
t = threading.Thread(target=contador3, args=(1,25))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contador3, args=(26,50))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contador2, args=(51,75))
listaHilos.append(t)
t.start()
t = threading.Thread(target=contador2, args=(76,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join()

tf= time.time() - t0

print(f'Tiempo de ejecucion: {tf}')
globalArrayNum.sort()
print(globalArrayNum)
print("-----------------------------")
"""
print("Usando 4 hilos")
print()

globalArrayNum = []
def contador3 ( inicio, fin, saltos ):
    for i in range (inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0

t0 = time.time()
listaHilos = []

inicio = 1
fin = inicio+25
    if fin>inicio:
        inicio=fin

for i in range(inicio, fin):
    t = threading.Thread(target=contador3, args=(1,100,25))
    listaHilos.append(t)
    t.start()
    for t in listaHilos:
        t.join()



tf= time.time() - t0

print(f'Tiempo de ejecucion: {tf}')
#globalArrayNum.sort()
print(globalArrayNum)
