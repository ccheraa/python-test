from modules.dummy import paragraph
import re
r = 'pattern|search'
s = paragraph
print('search', re.search(r, s))
print('findall', re.findall(r, s))
print('finditer:')
for x in re.finditer(r, s):
  print(' -', x)
print('match', re.match(r, s))
print('split', re.split(r, s))
print('sub', re.sub('(' + r + ')', '[[\\1]]', s))