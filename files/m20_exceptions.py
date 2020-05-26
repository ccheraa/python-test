import sys
def calc(a, b):
  print('calculating: a / b...')
  try:
    x = a / b
    print('  x calculated: x = a / b =', x)
  except NameError as e:
    print('  name error:', e)
  except TypeError as e:
    print('  type error:', e)
  except ZeroDivisionError as e:
    print('  zero division error:', e)
  except:
    e = sys.exc_info()[0]
    print('  unknown error:', e)
  else:
    print('  no errors!')
  finally:
    print('done.')
calc('a', 'b')
calc(1, 0)
calc(2, 3)