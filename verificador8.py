#ejercicio 1: calcular la eficiencia de una maquina
eficiencia_de_una_maquina, calor_caliente, calor_frio=0.0, 0.0, 0.0
#asignacion de valores
calor_caliente=500
calor_frio=200
#calculo
eficiencia_de_una_maquina=(calor_caliente - calor_frio)/calor_caliente
#mostrar valores
print("calor_caliente=", calor_caliente)
print("calor_frio=", calor_frio)
print("eficiencia_una_maquina=", eficiencia_de_una_maquina)
eficiencia_maxima=(eficiencia_de_una_maquina>0.6)
print("es eficiencia maxima", eficiencia_maxima)
