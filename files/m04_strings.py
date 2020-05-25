s1 = 'stRing'
s2 = "wiTh douBle quOtes"
s3 = '''multiline
string'''
s4 = 'another\nmultiline\nstring'
print('s1:', s1)
print('s2:', s2)
print('s3:', s3)
print('s4:', s4)
print('s[2]:', s1[2])
print('s2[-6:]:', s2[-6:])
print('len(s4):', len(s4))
print('s4.count(\'i\'):', s4.count('i'))
print('s2.upper():', s2.upper())
print('s2.lower():', s2.lower())
print('s2.title():', s2.title())
print('s2.capitalize():', s2.capitalize())
print('s2.split():', s2.split(' '))
print('s4.splitlines():', s4.splitlines())
print('s2.replace():', s2.replace('o', '00').replace('O', '00'))
print('dou in s1:', 'dou' in  s1, ' *  dou in s2:', 'dou' in  s2)
print('dou not in s1:', 'dou' not in  s1, ' *  dou not in s2:', 'dou' not in  s2)
print('s1 + s2:', s1 + s2)

# formatting
f1 = 'my name is {}'
print(f1)
print(f1.format('Ash'))

f2 = 'my name is {}, and I\'m {}'
print(f2)
# print(f2.format('Ash')) => error
print(f2.format('Ash', 30))

f3 = 'my name is {1}, and I\'m {0}'
print(f3)
print(f3.format(30, 'Ash'))

f4 = 'my name is {name}, and I\'m {age}, I\'m worth ${worth:.2f}'
print(f4)
print(f4.format(age=30, name='Ash', worth=1.5))
