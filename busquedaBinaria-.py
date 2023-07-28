def binsearch(A, x, low, hi):
  ans = None
  #print(low, hi)

  if low == hi: ans = False
  elif low + 1 == hi: ans = A[low] == x
  else:
    mid = low + ((hi - low) >> 1) # mid = (low+hi)//2
    if A[mid] == x: ans = True
    elif A[mid] > x: ans = binsearch(A, x, mid, hi)
    else: ans = binsearch(A, x, low, mid)
  return ans

l = [3, 6, 10, 14, 19, 21, 22, 22, 27, 31, 43]
l.reverse()
print(binsearch(l, 10, 0, 11))
print(binsearch(l, 24, 0, 11))
