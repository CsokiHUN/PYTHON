Nums = []

for i in range(2):
  num = None
  while not num:
    try:
      num = int(input('Adj meg egy ' + (i == 0 and 'kisebb' or 'nagyobb') + ' pozitív egész számot: '))
      if num < 0:
        num = None
        print('Megadott szám nem pozitív')
      Nums.append(num)
    except:
      print('Megadott szám hibás')

for i in range(Nums[0], Nums[1]):
  if i % 2 == 0:
    print(i)
