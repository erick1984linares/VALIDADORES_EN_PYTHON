#INPUT
comprador=input("ingrese el nombre del comprador:")
cantidad=int(input("ingrese el numero de productos:"))
pp=float(input("ingrese el precio de cada producto:"))

#PROCESSING
Total=(cantidad * pp)

#VERIFICADOR
cliente_satisfecho=(Total<=200)

#OUTPUT
print("#########################")
print("# TIENDA - LINARES ")
print("#########################")
print("#")
print("# Comprador               :     ", comprador)
print("# cantidad de productos   :     ", cantidad)
print("# Precio de cada producto : s/  ", pp)
print("# Total                   : s/  ", Total)
print("########################")
print("¿cliente satisfecho?", cliente_satisfecho)
