n = int(input("Deseja digitar quantos numeros?"))

nomes = []

for x in range(n):
  nomes.append(input("Insira um nome: "))

print("\n")

for x in range(n):
  
  print(nomes[x], len(nomes[x]))

print("\n")
print(nomes, len(nomes))
print("\n")
print(soma)
