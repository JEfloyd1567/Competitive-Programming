#planteando solucion al problema 11280 judge online (https://onlinejudge.org/external/112/11280.pdf)
#Juan Esteban floyd
#implementacion de bellman ford basada en la de la pagina: https://www.cramirez.info/teaching/agra/2021-2
#se crea el grafo, con bellman ford se verifican las conexiones de cada una de las aristas para posibles caminos mas cortos
from sys import stdin
from collections import deque

def bellmanFordOpt2(s):
    global d, p, G, W, diccionario, listaConsultas, cant
    n, ans, cola = len(G), True, deque()
    d = [float('inf') for _ in range(n)]
    p = [-1 for _ in range(n)]
    enCola = [False for _ in range(n)]
    conteo = [0 for _ in range(n)]
    d[s] = 0
    cola.append(s)
    enCola[s] = True
    while ans and len(cola) > 0:
        u = cola.popleft()
        enCola[u] = False
        for v in G[u]:
            if d[v] > d[u] + W[u][v]:
                d[v], p[v] = d[u] + W[u][v], u
                if not enCola[v]:
                    cola.append(v)
                    enCola[v] = True
                    conteo[v] += 1
                    if conteo[v] > n:
                        ans = False
    return ans, d, p

def main():
    global G, W, diccionario, listaConsultas, cant
    casos=int(input())
    indicador = 1
    for i in range(casos):
        print("Scenario #" + str(indicador))
        cant = int(input())
        listaCiudades=[]
        diccionario={}
        G=[[] for _ in range(cant)]
        W=[[] for _ in range(cant)]
        for k in range(cant):
            ciudad = stdin.readline().strip()
            listaCiudades.append(ciudad)
        for k in range(len(listaCiudades)):
            diccionario[listaCiudades[k]]=k
        conexiones=int(input())
        for k in range(conexiones):
            conexion = list(map(str,stdin.readline().strip().split()))
            clave=diccionario[conexion[0]]
            clave2=diccionario[conexion[1]]
            peso= int(conexion[2])
            G[clave2].append(clave)
            G[clave].append(clave2)
            W[clave2].append(peso)
            W[clave].append(peso)
        listaConsultas= list(map(int,stdin.readline().strip().split()))
        print(diccionario)
        print(G,W)
        print(listaConsultas)
        for j in range(len(listaConsultas)):
            flag, camino, predecedor = bellmanFordOpt2(0)
            if(flag):
                print("Total cost of flight(s) is $" + str(camino))
            else:
                print("No satisfactory flights")
        indicador += 1
main()