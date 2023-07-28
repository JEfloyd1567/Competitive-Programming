"""
The binary search

A = [0..N)
"""

def binary_search(A, x, low, hi):
    
    ans = None
    if (low + 1 == hi): ans = low
    else:
        mid = ((low + hi) >> 1)

        if (A[mid] <= x): ans = binary_search(A, x, mid, hi)
        else: ans = binary_search(A, x, low, mid)

    return ans

A = [1, 4, 6, 10, 10, 10, 10, 10, 10, 15, 26, 30]
x = 10

pos_left = binary_search(A, x, 0, len(A))

# Si el elemento esta, lo primero es correr la busqueda binaria y la posición que retorne (pos)
# para saber si el la del elemento como tal, se deberá hacer el siguiente chequeo.
# A[pos] == x

print("A[0, N):", A[pos_left] == x, A[pos_left], pos_left ) 

"""
Binary Search con intervalo abierto hacia izquierda
A = (low, hi]
"""

def binary_search1(A, x, low, hi):
    
    ans = None
    if (low + 1 == hi): ans = hi
    else:
        mid = ((low + 1 + hi) >> 1)

        if (A[mid] < x): ans = binary_search1(A, x, mid, hi)
        else: ans = binary_search1(A, x, low, mid)

    return ans

A = [1, 4, 6, 10, 10, 10, 10, 10, 10, 15, 26, 30]

pos_right = binary_search1(A, x, -1, len(A)-1)

print("A(-1, N-1]:", A[pos_right] == x, A[pos_right], pos_right)