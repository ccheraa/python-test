_i = 5
_f1 = 5.1
_f2 = 4.9
_c1 = 1+0j
_c2 = 1j
print('i:', type(_i), '=', _i)
print('f1:', type(_f1), '=', _f1)
print('f2:', type(_f2), '=', _f2)
print('c1:', type(_c1), '=', _c1)
print('c2:', type(_c2), '=', _c2)

# conversion
print('conversion:')
f = float(_i)
print('f from _i:', type(f), '=', f)
# f = float(c1) => error
i = int(_f1)
print('i from _f1:', type(i), '=', i)
i = int(_f2)
print('i from _f2:', type(i), '=', i)
# i = int(c1) => error
c = complex(_i)
print('c from _i:', type(c), '=', c)
c = complex(_f1)
print('c from _f1:', type(c), '=', c)
c = complex(_f2)
print('c from _f2:', type(c), '=', c)
