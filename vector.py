import math

def add(u, v):    
    return [a + b for a, b in zip(u, v)]
	
def sub(u, v):
    return [a - b for a, b in zip(u, v)]

def eq(u, v):
    return all([a == b for a, b in zip(u, v)])

def length_squared(u):
    return sum([a ** 2 for a in u])

def length(u):
    return math.sqrt(length_squared(u))

def scale(u, v):
    return [a * b for a, b in zip(u, v)]

def scale_by_scalar(u, scalar):
    return [a * scalar for a in u]

def dist(u, v):
    return length(sub(v, u))

def dist_squared(u, v):
    return length_squared(sub(v, u))

def norm(u):
    return scale_by_scalar(u, 1.0 / length(u))

def setlength(u, l):
    return scale_by_scalar(u, l / length(u))

def norm(u):
    return setlength(u, 1)

def movetowards(pos, dest, stepsize):
    if dist(pos, dest) <= stepsize:
        return dest
    else:
        d = sub(dest, pos)
        d = setlength(d, stepsize)
        return add(pos, d)
		
m = [1, 2] # monster position
p = [3, 4] # player position

# let monster move towards the player with
# a stepsize of 2
for i in range(0,3):
	m = movetowards(m, p, i)
	print m
# => m is now [1.70, 2.70]