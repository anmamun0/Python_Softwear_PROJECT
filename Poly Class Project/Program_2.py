#Made a program for slove eqardratic mathmatics

class Eqardratic_Equeation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def summari(self):

        import math
        d = (self.b)**2 - 4*(self.a*self.c)

        if d <0:
            print('Roots are imaginary')
        else:
            x1 = (-self.b + math.sqrt(d))/2
            x2 = (-self.b - math.sqrt(d))/2
            print(f'\nThe result is- \n {x1}\n{x2}\n')

one = int(input('Type a of number - '))
two = int(input('Type b of number - '))
three = int(input('Type c of number - '))


ee = Eqardratic_Equeation(one, two, three)
ee.summari()
