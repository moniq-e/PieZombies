import math
from playerClass import Initial

def kb(one, two, force):
	a = one.x
	b = one.y
	c = two.x
	d = two.y

	discop = math.sqrt(math.pow(c - a, 2) + math.pow(d - b, 2))

	finalpos = (force / discop)

	x = c + (finalpos * (c - a))
	y = d + (finalpos * (d - b))

	return Initial(x, y)