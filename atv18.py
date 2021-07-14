n1 = float(input("Digite o tamnho do arquivo em MB "))
n2 = float(input("Digite a velocidade em Mbps: "))


tempo = (n1/(n2/8))/60


print ("O tempo é:",round(tempo,2), "minutos")
