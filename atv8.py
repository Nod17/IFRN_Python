import math

n1 = float(input("Digite horas no formato hh.mm: "))
vh = float(input("Digite valor hora: "))

n2 = math.floor(n1)
n3 = (n1 - n2)*100
res = (n3/60)+n2

res1 = res*vh




print ("A valor é:", res1)

