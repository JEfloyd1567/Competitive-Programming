def binsearch(A, x):
  ans, N = False, len(A)

  if N != 0:
    low, hi = 0, N
    while low + 1 != hi:
      mid = low + ((hi - low) >> 1) # (hi + low) / 2
      #print(low, mid, hi)
      if A[mid] <= x:
        low = mid
      else:
        hi = mid
    ans = A[low] == x
  return ans

l = [3, 6, 10, 14, 19, 21, 22, 22, 27, 31, 43]
print(binsearch(l, 10))
print(binsearch(l, 24))
