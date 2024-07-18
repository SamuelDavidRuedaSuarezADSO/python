# 4. Escribir un programa que calcule el área de un triángulo:
# Base = 7 altura = 4 área del triángulo = (base * altura)/2

class area():
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def calArea(self):
        print("El area del triangulo es ", (self.b * self.a)/2)

trin = area(7,4)

trin.calArea()