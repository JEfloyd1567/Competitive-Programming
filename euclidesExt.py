def euclides(a, b):
	if(b == 0):
		ans = a 
	else:
		ans = euclides(b, a % b)
	return ans

def euclidesExt(a, b):
	if(b == 0):
		ans = (a, 1, 0)
	else:
		q, r = a // b, a % b
		d, ss, tt = euclidesExt(b, r)
		ans = (d, tt, ss - q * tt)
	return ans 

def euclidesIter(a, b):
	while(b != 0):
		a, b = b, a % b
	return a 
	
def euclidesExtIter(a, b):
	s, t, ss, tt = 1, 0, 0, 1
	while(b != 0):
		q, r = a // b, a % b
		a, s, t, b, ss, tt = b, ss, tt, r, s - ss * q, t - tt * q
	return a, s, t