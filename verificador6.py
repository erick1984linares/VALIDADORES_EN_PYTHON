#ejercicio 6: calcular el area de n hexagono regular
area_de_un_hexagono, apotema, semiperimetro_de_la_base=0.0, 0.0, 0.0
#asignacion de valores
apotema=14
semiperimetro_de_la_base=18
#calculo
area_de_un_hexagono=(apotema*semiperimetro_de_la_base)/2
#mostrar valores
print("apotema=", apotema)
print("semiperimetro_de_la_base=", semiperimetro_de_la_base)
print("area_de_un_hexagono=", area_de_un_hexagono)
mi_casa_es_un_hexagono=(area_de_un_hexagono<126)
print("es mi casa un hexagono:", mi_casa_es_un_hexagono)
