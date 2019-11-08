#volumen de un recipiente cilindrico
volumen,altura,radio,pi=0.0,0.0,0.0,0.0

#asignacion de valores
altura=1.2
radio=0.9
pi=3.14

#calculo
volumen=(pi*(radio**2)*altura)

#mostrar valores
print("El valor de la altura es:", altura)
print("El valor del radio es:", radio)
print("El valor de pi es:", pi)
print("El valor del volumen del cilindro es:", volumen)


#verificador 2
recipiente_pequeño=(volumen<4.4)
print("El volumen del recipiente es muy pequeño:",recipiente_pequeño)
