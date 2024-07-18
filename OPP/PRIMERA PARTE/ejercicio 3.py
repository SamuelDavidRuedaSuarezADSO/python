# 3. Un programa que lea 4 números y calcule la media.
# Media= (num1 + num2 + num3 + num4)/4

class media():
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    def calMedia(self):
        media = (self.num1 + self.num2 + self.num3 + self.num4)/4
        print("La media es: ", media)

nums = media(2,3,4,5)

nums.calMedia()