#tiempo de vuelo de una pelota lanzada desde el suelo
velocidad_inicial,gravedad,elevacion,tiempo_vuelo=0.0,0.0,0.0,0.0

#asignacion de valores
velocidad_inicial=50
gravedad=9.8
elevacion=0.8

#calculo
tiempo_vuelo=((2*velocidad_inicial*elevacion)/gravedad)

#mostrar resultados
print("el valor de la velocidad inicial es:",velocidad_inicial,"m/s")
print("el valor de la aceleracion de la gracedad es",gravedad,"m/s")
print("el angulo de elevacion es 53º y el valor usado es su seno(sen53º):",elevacion)
print("el valor del tiempo de vuelo de la  pelota es:",tiempo_vuelo,"s")

#verificador 7
tiempo_bajo=(tiempo_vuelo<5)
print("El tiempo de vuelo es bajo:",tiempo_bajo)
