#input
peso=float(input("Ingrese el peso de la persona(en kg):"))
altura=float(input("ingrese la altura de la persona (en m):"))

#processing
imc=peso/altura**2

#VERIFICADOR
sobre_peso=(imc>26)

#output
print("                                                 ")
print("#################################################")
print("#    CALCULADORA DE INDICE DE MASA CORPORAL     #")
print("#################################################")
print("# El valor del peso es:",peso,"kg")
print("# El valor de la altura es:",altura,"m")
print("#-----------------------------------------------#")
print("# El valor del IMC es:", imc)
print("#################################################")
print("El valor normal oscila entre 18.5 – 24.9")
print("mas que eso es obesidad, menos significa delgadez")
print("#################################################")
print("¿sobre peso?", sobre_peso)
