import time
import requests
from threading import Thread


def hacerrequest(direc, cantidad):
    for i in range(cantidad):
        requests.get(url = direc)
        print("HTTP GET", direc)
    return

#define la URL a atacar
URL = 'http://localhost/script'

#define cantidad de request
num_request = 100000

#define cantidad de threads a disparar
t1 = Thread(target=hacerrequest, args=(URL, num_request//5,))
t2 = Thread(target=hacerrequest, args=(URL, num_request//5,))
t3 = Thread(target=hacerrequest, args=(URL, num_request//5,))
t4 = Thread(target=hacerrequest, args=(URL, num_request//5,))
t5 = Thread(target=hacerrequest, args=(URL, num_request//5,))

#marca tiempo de inicio
start = time.time()

#levanta los threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

#espera a que finalice el anterior.
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

#marca tiempo de finalización
end = time.time()

tiempo = end - start
print("Tiempo consumido: ", tiempo)


