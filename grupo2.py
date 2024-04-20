import ctypes
import time
import matplotlib.pyplot as plt
import statistics
import numpy as np
def Moving_Average_Py_No_Numpy(Vin, N, W):
    i = 0
    sum = 0
    for i in range(K):
        sum += Vin[i]

    # Compute MA from index K
    for i in range(W, N):
        sum -= Vin[i - W]
        sum += Vin[i]
        Vout1[i] = sum / W
        return Vout1

def Moving_Average_Py_Numpy(Vin, N, W):
    i = 0
    Vout2 = []
    while i < N - W + 1:

        promedio = round(np.sum(Vin[i:i+W]) / W, 2)
        Vout.append(promedio)
        i += 1
    return Vout2

if __name__ == '__main__':
    lib = ctypes.CDLL('./moving_average.so')
    lib.Moving_Average_C.argtypes = [np.ctypeslib.ndpointer(dtype = np.int),ctypes.c_int,ctypes.c_int, ctypes.c_int, np.ctypeslib.ndpointer(dtype = np.float)]
    N = {16,32,64,128,256,512,1024,2048,4096,8192,16384}
    iter = 19
    lista_c = []
    lista_py_no_numpy= []
    lista_py_numpy= []
    for it in range(iter):
        tic = time.perf_counter()
        lib.euler(N)
        toc = time.perf_counter()
        lista_c.append((toc-tic)*1e6)
        tic = time.perf_counter()
        euler(N)
        toc = time.perf_counter()
        lista_py.append((toc-tic)*1e6)
        tic = time.perf_counter()
        lib.euler(N)
        toc = time.perf_counter()
        lista_c.append((toc-tic)*1e6)

    print(statistics.median(lista_c))
    print(statistics.median(lista_py_no_numpy))
    print(statistics.median(lista_py_numpy))

    plt.plot(lista_c)
    plt.plot(lista_py_no_numpy)
    plt.plot(lista_py_numpy)
    plt.grid()
    plt.legend(["Time C","Time Python No Numpy","Time Python Numpy"])
    plt.xlabel("Iteraciones")
    plt.ylabel("Tiempo [us]")
