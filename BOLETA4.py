#INPUT
nombre_del_comprador=input("ingrese el nombre del comprador:")
cantidad_de_pasajes_vendidos=int(input("ingrese la cantidad de pasajes vendidos:"))
precio_del_pasaje=int(input("ingrese el precio del pasaje:"))
igv=int(input("ingrese el igv:"))

#PROCESSING
total=((precio_del_pasaje + igv)*cantidad_de_pasajes_vendidos)

#VERIFICADOR
pasajeros_satisfechos=(total==90)

#OUTPUT
print("#######################")
print("#EMPRESA DE TRANSPORTES OLTURSA")
print("#######################")
print("#")
print("#nombre del comprador          :", nombre_del_comprador)
print("#cantidad de pasajes vendidos  :", cantidad_de_pasajes_vendidos)
print("#precio del pasaje             :", precio_del_pasaje)
print("#igv                           :", igv)
print("#total                         :", total)
print("#######################")
print("¿pasajeros satisfechos?", pasajeros_satisfechos)
