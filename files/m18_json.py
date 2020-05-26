from modules.dummy import d_json
import json
x = d_json
y = json.loads(x);
print('python:', y)
car = {
  'brand': 'volkswagon',
  'model': 'golf',
  'year': 2006,
  'factories': [
    'germany',
    'france',
    'brazil'
  ]
}
x = json.dumps(car, indent=2, separators=(';', ' = '))
print('json:', x)
x = json.dumps(car, separators=(',', ':'), sort_keys=True)
print('json:', x)