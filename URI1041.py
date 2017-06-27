entrada = input()
valores = entrada.split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

lista = [a,b,c]

lista.sort()

for x in lista:
	print (x)
	
print ("")	
print (a)
print (b)
print (c)
