import math

entrada = input()

valor = entrada.split()

a =  float(valor[0])
b =  float(valor[1])
c =  float(valor[2])

delta = (b)**2-4*(a)*(c)

if (delta >= 0 and a > 0):
	x1 = (-(b) + math.sqrt(delta)) / (2*(a))
	x2 = (-(b) - math.sqrt(delta)) / (2*(a))
	print ("R1 = %0.5f\nR2 = %0.5f" % (x1, x2))
else:
	print ("Impossivel calcular")

#Mateus Sousa


