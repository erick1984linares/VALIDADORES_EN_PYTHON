#trabajo realizado sobre un bloque
trabajo,fuerza,distancia,masa,aceleracion=0.0,0.0,0.0,0.0,0.0

#asignar valores
masa=12
aceleracion=5
distancia=16

#calculo
fuerza=(masa*aceleracion)
trabajo=(fuerza*distancia)

#mostrar valores
print("el valor de la masa es:",masa,"kg")
print("el valor de la aceleracion es:",aceleracion,"m/s")
print("el valor de la fuerza es:",fuerza,"N")
print("el valor del trabajo realizado al desplazar el bloque es:",trabajo,"Joules")

#verificador 8
trabajo_alto=(trabajo>900)
print("El trabajo es alto:",trabajo_alto)
