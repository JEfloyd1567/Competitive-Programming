def phi(A, N, n, k, B):
  '''
  complejidad temporal = O(n*2^n)
  comlejidad espacial = O(n)
  '''
  if(n == N):
    if(k == 0):
      print(B)
  else:
    phi(A, N, n + 1, k, B)
    if(len(B) == 0 or B[-1] <= A[n]):
      B.append(A[n])
      phi(A, N, n + 1, k - 1, B)
      B.pop()

A=[-1,5,3]
phi(A,len(A),0, 2, [])

