#Made a program for Triangle Area

class Triangale_Area:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def summari(self):
        import math

        if (self.a+self.b)>self.c and (self.a+self.c)>self.b and (self.b+self.c)>self.a:
            s = (self.a+self.b+self.c)/2
            area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
            print(f"The Traingle Area is  - {area}")
        else:
            print('Ractangle is not possible')

one = int(input('Type a of number - '))
two = int(input('Type b of number - '))
three = int(input('Type c of number - '))


ee =Triangale_Area(one, two, three)
ee.summari()
