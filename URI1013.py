entrada = input()
partes = entrada.split()

val1 = int(partes[0])
val2 = int(partes[1])
val3 = int(partes[2])

maiorAB = (val1+val2+abs(val1-val2)) / 2
maiorC = (maiorAB + val3 + abs(maiorAB - val3)) / 2

print ("%d eh o maior" % maiorC)

#Mateus Sousa
