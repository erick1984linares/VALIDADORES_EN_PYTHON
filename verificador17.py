#calcular el area de un abanico(sector circular)
area,radio,angulo,pi=0.0,0.0,0.0,0.0

#asiganacion de valores
radio=12
angulo=60
pi=3.14

#calculo
area=((pi*(radio**2)*angulo)/360)

#mostrar valores
print("el valor del radio es:",radio,"m")
print("el valor del angulo es:",angulo,"grados")
print("el valor de pi es:",pi)
print("el valor del area del abanico es:",area,"m")

#verificaador 4
area_grande=(area>75)
print("El abanico tiene area grande:",area_grande)
