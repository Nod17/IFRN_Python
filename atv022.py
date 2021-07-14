import math

n1 = float(input("Digite horas no formato hhh.mm: "))
vh = float(input("Digite valor hora: "))

n2 = math.floor(n1)
n3 = (n1 - n2)*100
res = (n3/60)+n2

res1 = res*vh

inss=res1*0.10
fgts=res1*0.11


if (res1<= 1500) and (res1>900):
    desc = 5
    ir=res1*0.05
    liq = res1-inss-ir

if (res1<= 2500) and (res1>1500):
    desc = 10
    ir=res1*0.10
    liq = res1-inss-ir

if (res1> 2500):
    desc = 20
    ir=res1*0.20
    liq = res1-inss-ir

if (res1<= 900):
    desc = 0
    ir="isento"
    liq = res1-inss

tdesc=ir+inss

print ("Salario Bruto    (",n1,"*",vh,"):     R$ {:.2f}".format(res1))
print ("    (-)IR (",desc,"%)       : R$", ir)
print ("    (-)INSS (10%)        : R$ {:.2f}".format(inss))
print ("    FGTS (11%)           : R$ {:.2f}".format(fgts))
print ("    toltal de descontos  : R$ {:.2f}".format(tdesc))
print ("    Salario Liquido      : R$ {:.2f}".format(liq))

