# 7. Escribir un programa que calcule el volumen de una esfera:
# Radio = 3 volumen de la esfera = 4/3 * PI * radio˄3

import math

class volumen():
    def __init__(self,radio):
        self.radio = radio
    def calVolum(self):
        volumen = (4/3)*math.pi*(self.radio**3)
        print("El volumen es igual", volumen)

esfera = volumen(3)

esfera.calVolum()