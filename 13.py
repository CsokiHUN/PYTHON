num = None
while not num:
  try:
    num = int(input('Adj meg egy pozitív egész számot: '))
    if num < 0:
      num = None
      print('Megadott szám nem pozitív')
  except:
    print('Megadott szám hibás')

for i in range(num):
  print((i % 2 == 0) and "1" or "0", end="")