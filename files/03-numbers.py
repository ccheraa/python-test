_i = 5
_f1 = 5.1
_f2 = 4.9
_c1 = 5+0j
_c2 = 5j
_s1 = '5'
_s2 = '5.5'
_s3 = '5 5'
print('i:', type(_i), '=', _i)
print('f1:', type(_f1), '=', _f1)
print('f2:', type(_f2), '=', _f2)
print('c1:', type(_c1), '=', _c1)
print('c2:', type(_c2), '=', _c2)
print('s1:', type(_s1), '=', _s1)
print('s2:', type(_s2), '=', _s2)
print('s3:', type(_s3), '=', _s3)

# conversion
print('conversion:')

f = float(_i)
print('f from _i:', type(f), '=', f)
f = float(_s1)
print('f from _s1:', type(f), '=', f)
f = float(_s2)
print('f from _s2:', type(f), '=', f)
# f = float(_s3) => error
# f = float(c1) => error

i = int(_f1)
print('i from _f1:', type(i), '=', i)
i = int(_f2)
print('i from _f2:', type(i), '=', i)
i = int(_s1)
print('i from _s1:', type(i), '=', i)
# i = int(_s2) => error
i = int(float(_s2))
print('i from float from _s2:', type(i), '=', i)
# i = int(c1) => error

c = complex(_i)
print('c from _i:', type(c), '=', c)
c = complex(_f1)
print('c from _f1:', type(c), '=', c)
c = complex(_f2)
print('c from _f2:', type(c), '=', c)
c = complex(_s1)
print('c from _s1:', type(c), '=', c)
c = complex(_s2)
print('c from _s2:', type(c), '=', c)

s = str(_i)
print('s from _i:', type(s), '=', s)
s = str(_f1)
print('s from _f1:', type(s), '=', s)
s = str(_f2)
print('s from _f2:', type(s), '=', s)
s = str(_c1)
print('s from _c1:', type(s), '=', s)
s = str(_c2)
print('s from _c2:', type(s), '=', s)
