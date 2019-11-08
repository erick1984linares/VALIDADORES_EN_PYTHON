#input
velocidad_inicial=int(input("Ingrese el valor de la velocidad inicial:"))
aceleracion=int(input("Ingrese el valor de la aceleracion:"))
tiempo=int(input("Ingrese el valor del tiempo:"))

#processing
velocidad_final=velocidad_inicial+(aceleracion*tiempo)

#VERIFICADOR
carro_en_baja_velocidad=(velocidad_final<5)

#output
print("                              ")
print("############################################")
print("# CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL")
print("############################################")
print("#Velocidad inicial    :",velocidad_inicial)
print("#Aceleracion          :",aceleracion)
print("#Tiempo               :",tiempo)
print("--------------------------------------------")
print("#Velocidad final del auto :  ",velocidad_final,"km/h")
print("############################################")
print("¿carro en baja velocidad?", carro_en_baja_velocidad)
