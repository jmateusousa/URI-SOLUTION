entrada = input()
lista = entrada.split()

codigo = lista[0]
quantidade = lista[1]

dirct = {'1':'4.00', '2':'4.50', '3':'5.00', '4':'2.00', '5':'1.50'}

total = float(dirct[codigo]) * int(quantidade)

print ("Total: R$ %0.2f" % total)
