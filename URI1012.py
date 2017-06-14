entrada = input()
partes = entrada.split()

A = float(partes[0])
B = float(partes[1])
C = float(partes[2])

pi = 3.14159

triangulo = (A * C) / 2
circulo = pi * (C*C)
trapezio = C*(A+B) / 2
quadrado = B*B
retangulo = A * B

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))
