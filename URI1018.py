valor = int(input())

resto = 0
contador = valor

while (contador > 0):
	
	if (contador >= 100):
		resto = contador%100
		cedulas = contador/100
		contador = resto
		print ("%d nota(s) de R$ 100,00" % cedulas)
	
	elif (contador >= 50):
		resto = contador%50
		cedulas = contador/50
		contador = resto
		print ("%d nota(s) de R$ 50,00" % cedulas)	
		
	elif(contador >= 20):
		resto = contador%20
		cedulas = contador/20
		contador = resto
		print ("%d nota(s) de R$ 20,00" % cedulas)	
		
	elif (contador >= 10):
		resto = contador%10
		cedulas = contador/10
		contador = resto
		print ("%d nota(s) de R$ 10,00" % cedulas)
		
	elif (contador >= 5):
		resto = contador%5
		cedulas = contador/5
		contador = resto
		print ("%d nota(s) de R$ 5,00" % cedulas)
	
	elif (contador >= 2):
		resto = contador%2
		cedulas = contador/2
		contador = resto
		print ("%d nota(s) de R$ 2,00" % cedulas)
	
	else:
		resto = contador%1
		cedulas = contador/1
		contador = resto
		print ("%d nota(s) de R$ 1,00" % cedulas)	
	

#Mateus Sousa
