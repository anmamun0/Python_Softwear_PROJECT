# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print('', end=' ')
#     for j in range(i):
#         print('*', end=' ' )
#     print()

# def fun(n):
#     for i in range(1,n+1):
#         print(' '*(n-i) + "* "*i)
    
# print(f'this /n {fun(5)}')


# for num in range(1,101):
#     if num>1:
#         for i in range(2, num):
#             if num%i==0:
#                 break
#         else:
#             print( num, end=',')

# def fun(n):
#     if n <= 1:
#         return n
#     else:
#          return fun(n-1)+ fun(n-2)
# n = 10
# for i in range(n):
#     print(fun(i), end=' ')

import argparse
import sys


def cals(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y




if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--x', type= float, help=' visite www.github.com/anmamun0')
    parse.add_argument('--y', type = float, help =' visite www.github.com/anmamun0')
    parse.add_argument('--o', type =str, help= ' visite www.github.com/anamun0')

    args = parse.parse_args()
    sys.stdout.write(str(cals(args)))