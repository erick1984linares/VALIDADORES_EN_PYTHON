#input
base_mayor=int(input("Ingrese el valor de la base mayor:"))
base_menor=int(input("Ingrese el valor de la base menor:"))
altura=int(input("Ingrese el valor de la altura:"))

#processing
area=((base_mayor+base_menor)*altura)/2

#VERIFICADOR
area_minima_para_el_trapecio=(area<=10)

#output
print("                                       ")
print("#######################################")
print("# CALCULADORA DEL AREA DE UN TRAPECIO  ")
print("#######################################v")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("------k i-----------------------------------")
print("#El valor del area del trapecio es:", area)
print("##########################################")
print("¿area minima para el trapecio?", area_minima_para_el_trapecio)
