import re

textfile = '''Phone = +1 (54848 66 88 8888)
Email: Northamerica@tata.com
webiste = www.northameraica.tata.com
Directions : View map fass
harry bai lakin  aiiiii
bahut hi badia aadmi haiaiin
Fax = + (654 566448 484 )
finall programmer mamun
'''

# findall, search , split, sub, finditer
# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Phone')
# patt = re.compile(r'mamun$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){2}')
patt = re.compile(r'ai{1} | Fax')

matches = patt.finditer(textfile)

for match in matches:
    print(match)


"""
[ ] A set of characters 
\ Singals a special sequence (can also be used to escape special characters)
. Any characters (except newline characters)
^ Starts with 
$ End with 
* Zero or more occurrences 
+ One or more occurrences 
{} Excactly the specified number of occurrences 
| Either or 
() Capture and group

special sequences 
\A 

"""
