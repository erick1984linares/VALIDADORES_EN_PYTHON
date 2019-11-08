#Energia potencial de una roca
energia_pot,masa,gravedad,altura=0.0,0.0,0.0,0.0

#asignacion de valores
masa=1.4
altura=21
gravedad=9.8

#calculo
energia_pot=(masa*gravedad*altura)

#mostrar valores
print("el valor de la masa es:",masa,"kg")
print("el valor de la altura es;",altura,"kg")
print("el valor de la aceleracion de la gravedad es:",gravedad,"m/s")
print("el valor de la energia potencial de la roca es:",energia_pot)

#verificador 5
energia_elevada=(energia_pot>=250)
print("La energia potencial de la roca es elevada:",energia_elevada)
