#input
dinero_inicial=float(input("ingrese el valor del dinero inicial:"))
dinero_mensual=float(input("Ingrese el dinero a ahorrar cada mes:"))
meses=float(input("ingrese el numero de meses a ahorrar:"))

#processing
dinero_final=dinero_inicial+(dinero_mensual*meses)

#VERIFICADOR
dinero_final_alto=(dinero_final>3000)

#output
print("                                                       ")
print("#######################################################")
print("#          CALCULADORA DE AHORRO DE DINERO             ")
print("#######################################################")
print("# El valor del dinero inicial es:",dinero_inicial,"s/.")
print("# El valor del dinero ahorrado por mes es:",dinero_mensual,"s/.")
print("# El numero de meses a ahorrar es:", meses)
print("#------------------------------------------------------")
print("# El dinero total al final del ahorro es de:",dinero_final,"s/.")
print("#######################################################")
print("¿dinero final alto?", dinero_final_alto)
