import time
import requests
from multiprocessing import Pool


def hacerrequest(direc,cantidad):
    for i in range(cantidad):
        requests.get(url = direc)
        print("HTTP GET", direc)
    return

#define la URL a atacar
URL = 'http://localhost/script'

#define cantidad de request
num_request = 100000

#define cantidad de procesos
num_processes = 4

#request por proceso
request_per_process = num_request // num_processes

if __name__ == '__main__':

    pool = Pool(processes=num_processes)
    start = time.time()
    r1 = pool.apply_async(hacerrequest, [URL, request_per_process])
    r2 = pool.apply_async(hacerrequest, [URL, request_per_process])
    r3 = pool.apply_async(hacerrequest, [URL, request_per_process])
    r4 = pool.apply_async(hacerrequest, [URL, request_per_process])
    pool.close()
    time.sleep(0.01)
    pool.join()
    end = time.time()
    print("Tiempo consumido: ", end - start)

