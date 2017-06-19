segundos = int(input())

minuto = (segundos%3600)/60
hora = int(segundos/60)/60
seg = segundos - (int(segundos/60) * 60)


print ("%d:%d:%d" % (hora, minuto, seg))

#Mateus Sousa



