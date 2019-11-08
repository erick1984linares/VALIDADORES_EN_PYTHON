#La presion sobre una placa de acero
presion,fuerza,area,masa,aceleracion=0.0,0.0,0.0,0.0,0.0

#asignacion de valores
masa=2.6
aceleracion=12.5
area=26

#calculo
fuerza=(masa*aceleracion)
presion=(fuerza/area)

#mostrar valores
print("el valor de la masa es:",masa,"kg")
print("el valor de la aceleracion es:",aceleracion,"m/s")
print("el valor de la fuerza es:",fuerza,"N")
print("el valor del area de la placa es:",area,"metros cuadrados")
print("el valor de la presion es:",presion,"Pa")

#verificador 6
presion_mayor=(presion>1.0)
print("La presion es mayor que la atmosferica:",presion_mayor)
