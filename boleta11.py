#input
primer_elemento=int(input("Ingrese el primer elemento de la sucesion:"))
ultimo_elemento=int(input("Ingrese el ultimo elemento de la sucesion:"))
total_elementos=int(input("Ingrese el numero total de elementos de la sucesion:"))

#processing
sumatoria=(primer_elemento+ultimo_elemento)*total_elementos/2

#VERIFICADOR
sumatoria_larga=(sumatoria>30)

#output
print("                                                                    ")
print("#####################################################################")
print("#     SUMATORIA DE UNA SUCESION ARITMETICA DE NUMEROS NATURALES     #")
print("#####################################################################")
print("# El valor del primer elemento es:", primer_elemento)
print("# El valor del ultimo elemento es:", ultimo_elemento)
print("# El total de elemntos es:",total_elementos)
print("#--------------------------------------------------------------------")
print("# El valor de la sumatoria de los elemntos de la sucesion es:",sumatoria)
print("#####################################################################")
print("                                                                     ")
print("¿sucesion larga?", sumatoria_larga)
