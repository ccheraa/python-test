print('[[ while ]]')
i = 1
while i <= 5:
  print('-', i)
  i += 1
print('break')
i = 1
while i <= 5:
  if i == 3 : break
  print('-', i)
  i += 1
print('continue')
i = 1
while i <= 5:
  i += 1
  if i == 4 : continue
  print('-', i - 1)
print('else')
i = 1
while i <= 5:
  print('-', i)
  i += 1
else:
  print('+', i)


print('[[ for ]]')
for x in range(1, 6):
  print('-', x)
print('string')
for x in 'string':
  print('-', x)
print('break')
for x in 'string':
  if x == 'i' : break
  print('-', x)
print('continue')
for x in 'string':
  if x == 'i' : continue
  print('-', x)
print('continue')
for x in 'string':
  print('-', x)
else:
  print('+', x)
