# define variables
a = 2
b = c = a + 5
(x, y, z) = (a, b, c)
s = 'c = ' + str(c)
print('a:', a)
print('b:', b)
print('c:', c)
print('x:', x)
print('y:', y)
print('z:', z)
print('s:', s)

# types
print('types')
a = 1
b = 1.0
c = 1+0j
d = "1"
e = [1]
f = (1,)
g = {1}
print('a:', type(a), '=', a)
print('b:', type(b), '=', b)
print('c:', type(c), '=', c)
print('d:', type(d), '=', d)
print('e:', type(e), '=', e)
print('f:', type(f), '=', f)
print('g:', type(g), '=', g)
