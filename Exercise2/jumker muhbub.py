# def an_mamun(other):
#     def decoredtor():
#         print('________________')
#         other()
#         print('__________________')
#     return decoredtor


# def printt():
#     print('This is mamun')

# dec = an_mamun(printt)
# dec()

# import re 

# mystr = '''Unable 
# to resolve configuration with compilerPath: 
# "gcc" [7/10/2023, 3:42:27 PM] Unable to 
# resolveconfiguration with compilerPath
# gcc Unable 01782-059949
# almamun@gmail.com
# to resolve configuration wiiiith compilerPath: 
# "gcc" [7/10/2023, 3:42:27 PM] 01948-904009 Unable to 
# resolveconfiguration wth compilerPath @gmail.com
#  23454@gmail.com gcc''' 

# patt = re.compile(r'[a-zA-Z0-9]+@([\w]+.com)')
# matches = patt.finditer(mystr)

# for mattch in matches:
#     print(mattch)

# from matplotlib import pyplot as plt

# x = [5,3,7,9]
# y = [9,7,4,3]
# plt.plot(x,y)
# plt.show()

for i in range(1,100):
    for n in range(2,i):
        if i%n == 0:
            break
    else:
        print(i)