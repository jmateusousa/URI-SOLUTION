from math import sqrt

xy1 = input()
xy2 = input()

p1 = xy1.split()
p2 = xy2.split()

distancia = sqrt(((float(p2[0]) - float(p1[0]))**2) + ((float(p2[1]) - float(p1[1]))**2))

print ("%0.4f" % distancia)
