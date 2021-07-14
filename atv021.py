n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

maior=n1

if (n2 >= maior):
        maior = n2        
if (n3 >= maior):
            maior = n3
        
print('Maior: ',maior)

menor = n1
if (n2 <= menor):
        menor = n2
if (n3 <= menor):
            menor = n3

print('Menor: ',menor)
