# 1. Escribir un programa que sume, reste, multiplique y divida dos números

class Calculadora ():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        res =  self.num1 + self.num2
        print("El resultado de la suma es " , res)

    def resta(self):
        res = self.num1 - self.num2
        print("El resultado de la resta es ", res)

    def multi(self):
        res = self.num1 * self.num2
        print("El resultado de la multiplicacion es ", res)

    def dividir(self):
        if self.num1 != 0 or self.num2 != 0:
            res = self.num1 / self.num2
            print("El resultado de la division es ", res)
        else:
            print("No se puede dividir pro cero")

nums = Calculadora(3,2)

nums.suma()
nums.resta()
nums.multi()
nums.dividir()








# 11. Escribir un programa que calcule el volumen de un elipsoide
# V = (4/3) * PI * a * b *c

# 12. Programa que muestre el pago de una llamada telefónica sabiendo que cada minuto cuesta $355
# pesos y un IVA de 20%.

# 13. Realice un algoritmo que a partir de proporcionarle la velocidad de un automóvil expresada en
# kilómetros por hora, proporcione la velocidad en metros por segundos.

# 14. Una farmacia aplica al precio de los remedios el 10% de descuento, hacer un programa que
# ingresando el costo de los medicamentos calcules el descuento y el precio final.

# 15. Hacer un diagrama para convertir de grados centígrados a grados Fahrenheit.

# 16. Elaborar un algoritmo para calcular el promedio final de la materia de algoritmos. Dicha
# calificación se compone de los siguientes porcentajes:
# • 55% del promedio final de sus calificaciones de los tres(3) parciales.
# • 30% de la calificación examen final y
# • 15% de la calificación trabajo final.

# 17. Dado el valor que un cliente paga por un producto, calcular qué valor corresponde al costo total del
# producto y cuánto es el valor del IVA. Considerando que el porcentaje del IVA puede variar en el
# tiempo y de un producto a otro, este dato se lee por teclado.

# 18. Calcular el sueldo de un empleado dados comodatos de entrada: el nombre, hrs. De trabajo y el
# pago en hora. Pagohora=15300

# 19. Un estudiante realiza cuatro exámenes. Realizar el pseudocódigo que representen el algoritmo
# correspondiente para obtener el promedio de las calificaciones obtenidas. las calificaciones van 1 a 5
# puntos.

# 20. Un vendedor recibe un sueldo base más el 10% de comisión sobre sus ventas. Si en un mes
# cualquiera hace tres ventas por valores: v1, v2 y v3, ¿cuánto recibirá por comisión? y ¿cuánto en total
# sueldo del vendedor?.