numbers = []

for i in range(3):
  inum = None
  while not inum:
    try:
      inum = int(input('Add meg a ' + str(i + 1) + '. számot: '))
    except:
      print('Hibás szám próbáld újra!')
  numbers.append(inum)

for i in numbers:
  counter = 0
  for k in numbers:
    if (k != i):
      counter += k
  print(i, (counter != i and "Nem " or "") + 'egyenlő a másik két számmal')