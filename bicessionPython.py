def f1(n): return (n * (n + 1))

def f2(n): return (n * (n + 1)) / 2

def bisectionInt(f, low, hi, x):
  ans, wans = None,None
  
  if low < hi:
    while low + 1 != hi:
      mid = low + ((hi - low) >> 1)
      print(low, mid, hi)

      if f(mid) <= x:
      	low = mid
      else:
      	hi = mid
    ans, wans = f(low), low
  return ans, wans

print(bisectionInt(f1, -10000, 10000, 100))
print(bisectionInt(f2, -10000, 10000, 100))

eps = 1e-8

def bisectionDouble(f, low, hi, x):
  ans, wans = None, None
  
  if low < hi:
    while abs(hi - low) > eps:
      mid = low + ((hi - low) / 2)
      #print(low, mid, hi)

      if f(mid) <= x:
      	low = mid
      else:
      	hi = mid
    ans, wans = f(low), low
  return ans, wans

print(bisectionDouble(f1, -10000, 10000, 0))
print(bisectionDouble(f2, -10000, 10000, 0))
