car = {
  'brand': 'volkswagon',
  'model': 'golf',
  'year': 2006
}

print('car:', car)
print('car[model]:', car['model'])
car['year'] = 2002
print('car.get(\'year\'):', car.get('year'))

print('car:')
for x in car:
  print(' -', x, '=>', car[x])
print('car values:')
for x in car.values():
  print(' -', x)
print('car keys:')
for x in car.keys():
  print(' -', x)
print('car items:')
for x in car.items():
  print(' -', x)
for (x, y) in car.items():
  print(' +', x, '=>', y)

print('car has model?', 'model' in car)
print('car has factory?', 'factory' in car)
print('len(car):', len(car))
car['factory'] = 'france'
print('car:', car)
print('car.pop(\'model\'):', car.pop('model'))
print('car:', car)
print('car.popitem():', car.popitem())
print('car:', car)