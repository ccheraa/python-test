a = -5
b = 0
if a > b:
  print('a is bigger')
elif a == b:
  print('a equals b')
else:
  print('b is bigger')

if b == 0: print('b equals 0')

print("A") if a > b else print("=") if a == b else print("B")