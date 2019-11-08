#INPUT
nombre_del_cliente=input("ingrese el nombre del cliente:")
precio_del_pantalon=int(input("ingrese el precio del pantalon:"))
precio_del_polo=int(input("ingrese el precio del polo:"))
precio_de_la_casdaca=int(input("ingrese el precio de la casaca:"))

#PROCESSING
total=(precio_de_la_casdaca + precio_del_pantalon + precio_del_polo)

#VERIFICADOR
descuentos_accesibles=(total==200)

#OUTPUT
print("###################################")
print("#TIENDAS - RIPLEY")
print("###################################")
print("#")
print("#nombre del cliente   :", nombre_del_cliente)
print("#precio del pantalon  :", precio_del_pantalon)
print("#precio del polo      :", precio_del_polo)
print("#precio de la casaca  :", precio_de_la_casdaca)
print("#total                :", total)
print("####################################")
print("¿descuentos accesibles?", descuentos_accesibles)
