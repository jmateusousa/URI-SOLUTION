entrada = input()
n_entrada = entrada.split()

a = int(n_entrada[0])
b = int(n_entrada[1])
c = int(n_entrada[2])
d = int(n_entrada[3])

if (b > c and d > a and c + d > a + b and c >= 0 and d >= 0 and a%2 == 0):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
	
#Mateus Sousa
