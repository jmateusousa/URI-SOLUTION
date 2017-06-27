notas = input()
lista = notas.split()

N1 = float(lista[0])
N2 = float(lista[1])
N3 = float(lista[2])
N4 = float(lista[3])

media = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10)

print ("Media: %0.1f" % media)

if (media >= 7.0):
	print ("Aluno aprovado.")
elif (media < 5.0):
	print ("Aluno reprovado.")
elif (5.0 <= media <= 6.9):
	print ("Aluno em exame.")
	exame = float(input())
	print ("Nota do exame: %0.1f" % exame)
	nota_final = (exame + media) / 2
	if (nota_final >= 5.0):
		print ("Aluno aprovado.")
	else:
		print ("Aluno reprovado.")
		
	print ("Media final: %0.1f" % nota_final)

