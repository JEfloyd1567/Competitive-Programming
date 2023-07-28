"""
The New Villa
https://uva.onlinejudge.org/external/3/321.pdf

BFS - State Space

"""

from collections import deque
from sys import stdin

def main():
    case = 1
    r, d, s = map(int, stdin.readline().split())
    while r != 0 or d != 0 or s != 0:
        obj, dist = 1 << r - 1, {}
        habAdy, lucesAdy = [[False for _ in range(11)] for _ in range(11)], [[False for _ in range(11)] for _ in range(11)]

        for i in range(d):
            u, v = map(int, stdin.readline().split())
            habAdy[u][v] = habAdy[v][u] = True
        for i in range(s):
            u, v = map(int, stdin.readline().split())
            lucesAdy[u][v] = True

        cola, flag = deque(), False
        cola.append((1, 1, []))
        dist[(1, 1)] = 0

        while not flag and len(cola) != 0:
            pos, conteo, pasos = cola.popleft()
            if pos == r and obj == conteo: flag = True
            else:
                # verificar posibilidades de desplazarse a otra habitación
                for i in range(1, r + 1):
                    # se verifica que haya un pasillo hacía la habitación i y que la luz en esa habitación esté
	            # encendida
                    if habAdy[pos][i] and ((conteo & (1 << i - 1)) == (1 << i - 1)):
                        npasos = list(pasos)
                        npasos.append(("move", i))
                        mov = (i, conteo, npasos)
                        if (i, conteo) not in dist:
                            cola.append(mov)
                            dist[(i, conteo)] = dist[(pos, conteo)] + 1

                # verificar posibilidades de encender o apagar una luz en otra habitación
                for i in range(1, r + 1):
	            # se verifica que haya un switch que permita encencer la luz de la habitación i
	            # y que no sea la misma habitación en la que se está ubicado
                    if lucesAdy[pos][i] and i != pos:
                        npasos = list(pasos)
                        mov = (pos, conteo ^ (1 << i - 1), npasos)
                        npasos.append(("on" if mov[1] > conteo else "off", i))
                        if (pos, mov[1]) not in dist:
                            cola.append(mov)
                            dist[(pos, mov[1])] = dist[(pos, conteo)] + 1
        print("Villa #%d" % case);
        if flag:
            print("The problem can be solved in %d steps:" % dist[(pos, conteo)])
            for (desc, hab) in pasos:
                if desc == "on": print("- Switch on light in room %d." % hab)
                elif desc == "off": print("- Switch off light in room %d." % hab)
                else: print("- Move to room %d." % hab)
        else:
            print("The problem cannot be solved.");
        print()
        stdin.readline()
        r, d, s = map(int, stdin.readline().split())
        case += 1

main()
