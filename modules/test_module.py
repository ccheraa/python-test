def d_list(*args):
  for i in range(len(args)):
    print('{} - {}'.format(str(i).zfill(2), args[i]))
def d_dict(**kws):
  for i in kws:
    print('{} - {}'.format(i, kws[i]))