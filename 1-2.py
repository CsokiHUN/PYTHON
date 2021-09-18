numbers = []

for i in range(3):
  inum = None
  while not inum:
    try:
      inum = int(input('Add meg a ' + str(i + 1) + '. számot: '))
    except:
      print('Hibás szám próbáld újra!')
  numbers.append(inum)
print('Legkisebb szám: ', min(numbers))
print('Legnagyobb szám: ', max(numbers))
