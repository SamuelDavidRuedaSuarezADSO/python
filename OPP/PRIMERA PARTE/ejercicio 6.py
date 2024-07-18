# 6. Escribir un programa que calcule la velocidad de un proyectil que 
# recorre 2 Km en 5 minutos. Expresar el resultado en metros/segundo. 
# Velocidad = espacio/tiempo.

class velocidad ():
    def __init__(self, espacio, tiempo):
        self.espacio = espacio
        self.tiempo = tiempo
    def calVelo(self):
        metro = self.espacio*1000
        seg = self.tiempo*60
        velo=metro/seg
        print("La velociada es igual a", velo , "M/s")

espacio = 2
tiempo = 5

proyectil = velocidad(espacio, tiempo)

proyectil.calVelo()