def p1():
  print('called')
p1()
def p2(name):
  print('name:', name)
p2('name')
def p3(fname, lname):
  print(fname, lname)
p3('Demman', 'CRUISE')
def p4(*args):
  print(args)
p4('Demman', 'CRUISE', '30')
def p5(**keywords):
  print(keywords)
p5(fname='Demman', lname='CRUISE', age='30')
def p6(*nums):
  r = 0
  for x in nums:
    r += x
  return r
print('sum 1,3,5,7,9 =', p6(1, 3, 5, 7, 9))
print('sum 1..10 =', p6(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
p7 = lambda x : x * 2
print('double 5 =', p7(5))
print('double 7 =', p7(7))
p8 = lambda x, y : x ** y
print('5 ^ 3 =', p8(5, 3))
print('7 ^ 2 =', p8(7, 2))
def p9(n):
  return lambda x : x * n
print('5 * 3 =', p9(3)(5))
print('7 * 2 =', p9(2)(7))