itens = []
valor = []

for x in range(2):
  itens.append(input("Insira um item: "))
  valor.append(float(input("Insira o valor R$: ")))

print("\n")


for x in range(2):
  print("Item:",itens[x], "Valor: R$",valor[x])
  print(len(itens[x]))


soma = sum(valor)

print("\n")
print("Valor total: R$",soma)

