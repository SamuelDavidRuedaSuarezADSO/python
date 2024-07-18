# 2. Escribir un programa que calcule el área de un rectángulo:
# lado1 = 3 lado2 = 4 área del rectángulo= lado1 * lado2

class area():
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def calArea(self):
        print("El area del rectangulo es ", self.l1 * self.l2)
    
rectangulo = area(3,4)

rectangulo.calArea()