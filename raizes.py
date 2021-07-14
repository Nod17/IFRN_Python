a = int(input("Digite o valor de a: "))

if a==0:
   print("Não possui raizes reais")
    
    

else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = b**2 - (4*a*c)

    if delta == 0:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        print ("Só possui uma raiz real: {}".format(x1))
    
    if delta > 0:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        print ("Raizes X1 = {}, X2 = {}".format(x1,x2))
    if delta < 0:
        print("Não possui raizes reais")
