#Cálculo de velocidad final de un auto
velocidad_final,velocidad_inicial,aceleracion,tiempo=0.0,0.0,0.0,0.0

#asignacion de valores
velocidad_inicial=12
aceleracion=5
tiempo=20

#calculo
velocidad_final=(velocidad_inicial+aceleracion*tiempo)

#mostrar valores
print("El valor de la velocidad inicial es:",velocidad_inicial)
print("El valor de la aceleración es:", aceleracion)
print("El valor del tiempo es:", tiempo)
print("El valor de la velocidad final es:", velocidad_final)

#verificador 1
velocidad_peligrosa=(velocidad_final>=100)
print("El auto va a una velocidad peligrosa:",velocidad_peligrosa)
