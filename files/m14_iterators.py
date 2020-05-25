s = 'banana'
print('loop:')
for x in s:
  print('-', x)
print('iterator:')
i = iter(s)
for x in range(len(s)):
  print('-', next(i))

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday']
class WeekDay:
  def __iter__(self):
    self.c = -1
    return self
  def __next__(self):
    if self.c < 30:
      self.c += 1
      global days
      return days[self.c % 7]
    else:
      raise StopIteration

a = WeekDay()
print('class:')
i = 0
for x in a:
  i += 1
  print(' {} - {}'.format(str(i).zfill(2), x))