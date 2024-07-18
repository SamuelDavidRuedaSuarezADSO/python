# 9. Escribir un programa que calcule el área y el volumen de un cilindro:
# A = (2 * (PI * r˄2)) + ((2 * PI * r) * h)
# V = (PI * r2) * h

import math

class calcular():
    def __init__(self, r, h):
        self.r = r
        self.h = h
    def area(self):
        print("El area es igual a" ,2 * (math.pi * (self.r ** 2)) + (2 * math.pi * self.r) * self.h)

    def volumen(self):
        print("El volumen es igual a", (math.pi * (self.r ** 2)) * self.h)

cilin = calcular(6,4)

cilin.area()
cilin.volumen()