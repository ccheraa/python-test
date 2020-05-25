l1 = ['apple', 'pineapple', 'banana']
l2 = ['japan', 'egypt', 'spain']
l3 = l1 + l2
print('l1[1]', l1[1])
print('l1[-1]', l1[-1])
print('l3[2:-1]', l3[2:-1])
print('l3:')
for x in l3:
  print('  -', x)
print('japan in l1:', 'japan' in l1)
print('japan in l3:', 'japan' in l3)
print('len(l3):', len(l3))
l3.append('tunisia')
l3.insert(1, 'orange')
l3.remove('banana')
del(l3[2])
print('l3:', l3)
l4 = l3
l5 = l3.copy()
l3.clear()
print('l3:', l3)
print('l4 = l3:', l4)
print('l5 = l3.copy():', l5)
l6 = [1, 2, 3]
print('l6:', l6)
l6.extend(l5)
print('l6:', l6)
