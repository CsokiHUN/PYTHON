num = None
while not num:
  try:
    num = int(input('Adj meg egy pozitív egész számot: '))
    if num < 0:
      num = None
      print('Megadott szám nem pozitív')
  except:
    print('Megadott szám hibás')

for i in range(0, num):
  if i % 3 == 0:
    print(i)
