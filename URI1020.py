d = int(input())

anos = d/365
meses = d%365/30
dias = d%365%30

print ("%d ano(s)\n%d mes(es)\n%d dia(s)" % (anos, meses, dias))
