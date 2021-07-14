import math

n1 = float(input("Digite horas no formato hhh.mm: "))
vh = float(input("Digite valor hora: "))

n2 = math.floor(n1)
n3 = (n1 - n2)*100
res = (n3/60)+n2

res1 = res*vh


ir=res1*0.11
inss=res1*0.08
sind=res1*0.05
liq = res1-ir-inss-sind


print ("+ Salario Bruto: R$ {:.2f}".format(res1))
print ("- Desconto IR (11%): R$ {:.2f}".format(ir))
print ("- Desconto INSS (8%): R$ {:.2f}".format(inss))
print ("- Desconto Sindicato (5%): R$ {:.2f}".format(sind))
print ("= Salario Liquido: R$ {:.2f}".format(liq))

