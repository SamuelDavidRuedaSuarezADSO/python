# 8. Escribir un programa que evalúe la siguiente expresión: (a+7*c)/(b+2-a)+2*b

class express():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def res(self):
        print((self.a+7*self.c)/(self.b+2-self.a)+2*self.b)

a = 3
b = 4
c = 15

expre = express(a,b,c)

expre.res()