lista = []
linha = []

nc = int(input('Quantas colunas? '))
nl = int(input('Quantas linhas? '))
for c1 in range(0, nl):
    linha = []
    for c2 in range(0, nc):
        n = int(input('Número L[{0}] C[{1}]: '.format(c1 + 1,c2 + 1)))
        linha.append(n)
    lista.append(linha)
print(lista)
