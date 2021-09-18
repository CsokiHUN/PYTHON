pair = True

for i in range(3):
  inum = None
  while not inum:
    try:
      inum = int(input('Add meg a ' + str(i + 1) + '. számot: '))
      if inum % 2 > 0:
        pair = False
    except:
      print('Hibás szám próbáld újra!')
print(pair and 'Mindhárom szám páros' or 'Nem páros mindhárhom szám')