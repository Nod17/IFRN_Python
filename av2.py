

notas = [[8, 3, 10, 6],[10, 2, 3, 4],[7, 8, 2, 6],[4, 9, 5, 7]]

i=5
tvar=0

for linha in notas:
    print(linha)
print("\n")

for linha in notas:
    i = i+1
    media = sum(linha)/len(linha)
    print("Media {}".format(i),"º Ano: ", media)
    
    for item in linha:
        tvar+=((item-media)**2)
    
    
    var=tvar/3
    dp=var**0.5
    print("Variância {}".format(i),"º Ano: ", var)
    print("Desvio padrão {}".format(i),"º Ano: ", dp,"\n")
    
