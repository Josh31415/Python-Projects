#! /usr/bin/python2.7

formula = raw_input("What is your formula")
ll = raw_input("What is the lower limit")
ul = raw_input("What is the upper limit")
rect = raw_input("How many rectangles do you want to use")
ill = float(ll)
iul = float(ul)
frect = float(rect)
d = iul - ill
h = d/frect
sol = 0.0
ans = 0.0
iy = 0.0
x = ill
g = 2
irect = int(frect)
sol = eval(formula)
ans = sol
ill = ill + h
for y in range(1, (irect)):
	sol = 0

	if g % 2 == 0: 
		x = ill
		sol = ((eval(formula)) * 4)
	else :
		x = ill
		sol = ((eval(formula)) * 2)
	ill = ill + h
	g = g + 1	
	ans = ans + sol
x = iul
sol = eval(formula)
ans = ans + sol
ans = ans * (h/3)
ill = ill + h
print (ans)

