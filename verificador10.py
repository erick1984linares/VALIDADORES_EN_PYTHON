#ejercicio 10: calcular el volumen de un tronco de cilindro
volumen_del_tronco_de_cilindro, altura5, radio1, radio2=0.0, 0.0, 0.0, 0.0
#asignacion de valores
altura5=21
radio1=3.2
radio2=5.2
#calculo
volumen_del_tronco_de_cilindro=(altura5*(radio1*radio1 + radio2*radio2 + radio1*radio2))/3
#mostrar valores
print("altura5=", altura5)
print("radio1=", radio1)
print("radio2=", radio2)
print("volumen de un trono de cilindro=", volumen_del_tronco_de_cilindro)
barril=(volumen_del_tronco_de_cilindro<377.44)
print("es barril:", barril)
