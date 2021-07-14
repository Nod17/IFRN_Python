lista = []#Lista para armazenar

for x in range(5):#Aqui eu vou pegando os valores
  lista.append(input("Produto: "))
  lista.append(float(input("Valor: ")))
y = 0#Criei essa variável para ir pulando de 2 em 2


for x in range(5):#Aqui eu vou mostrar
  print(f"Produto: {lista[y]} Valor: {lista[y+1]}")
  y = y+2
