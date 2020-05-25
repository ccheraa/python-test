import datetime as d
now = d.datetime.now()
print('now:', now)
print('year:', now.year)
print('dd-mm-yyyy:', now.strftime('%d-%m-%Y'))
bd = d.datetime(1989, 7, 13, 14, 59, 59)
print('bd:', bd)
print(bd.strftime('birthday on %A, %B %d, %Y, at %H:%M:%S'))