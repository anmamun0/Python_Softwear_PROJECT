#Made a program for Triangle Area

class Triangale_Area:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def summari(self):
        if self.a > self.b and self.a > self.c :
            print(f'Your Learge Number is - {self.a}')
        elif self.b > self.c :
            print(f'Your Learge Number is - {self.b}')
        else:
            print(f'Your learge Number is -{self.c}')

one = int(input('Type a of number - '))
two = int(input('Type b of number - '))
three = int(input('Type c of number - '))


ee =Triangale_Area(one, two, three)
ee.summari()
