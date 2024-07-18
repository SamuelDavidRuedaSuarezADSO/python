# 5. Escribir un programa que calcule la longitud y el área de una circunferencia: Radio = 4
# Longitud de la circunferencia = 2 * PI * radio
# Área de la circunferencia = PI * radio˄2

import math

class calculos ():
    def __init__(self, radio):
        self.radio = radio
    def longitud(self):
        print("La longitud es de: ", 2 * math.pi * self.radio)
    def area(self):
        print("El area es de: ", math.pi * self.radio ** 2)

circu = calculos(18)

circu.area()
circu.longitud()