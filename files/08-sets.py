s1 = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 = { 1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
s3 = { 0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
s4 = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
s5 = { 4, 8, 12, 16, 20, 24, 28, 32, 36, 40}
print('s1:', s1)
print('s2:')
for x in s2:
  print(' -', x)
print('3 in s2:', 3 in s2)
print('3 in s3:', 3 in s3)
s6 = {'apple', 'pineapple', 'banana'}
print('s6:', s6)
s6.add('orange')
s6.update(['orange', 'japan', 'egypt', 'spain'])
print('s6:', s6)
s6.remove('orange')
# s6.remove('strawberry') => error
s6.discard('strawberry')
print('s6:', s6)
print('len(s6):', len(s6))
print('s6.pop():', s6.pop())
print('s6:', s6)
s6.clear()
print('s6:', s6)
a = { 0, 1, 2, 3, 4}
b = { 2, 3, 4, 5, 6}
c = a.union(b)
d = a.intersection(b)
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('c = a \u222A b =', a.union(b))
print('d = a \u2229 b =', a.intersection(b))
print('a - b =', a.difference(b))
print('a \u2296 b =', a.symmetric_difference(b))
print('a \u2286 b =', a.issubset(b))
print('a \u2286 c =', a.issubset(c))
print('5 \u2208 a =', 5 in a)
print('5 \u2208 b =', 5 in b)