number = None

while not number:
  try:
    number = int(input('Adj meg egy egész számot: '))
  except:
    print('Hibás a megadott szám próbáld újra!')
print('Megadott szám osztható 3-mal vagy 5-tel: ', (number % 3 == 0 or number % 5 == 0) and 'Igen' or 'Nem')
