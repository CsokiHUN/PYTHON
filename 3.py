points = None

while not points:
  try:
    points = int(input('Add meg a dolgozat pontszámát: '))
  except:
    print('Hibás a megadott pontszám próbáld újra!')

print('Elért eredményed: ', end="")
if points < 50:
  print(1)
elif points >= 50 and points < 60:
  print(2)
elif points >= 60 and points < 70:
  print(3)
elif points >= 70 and points < 85:
  print(4)
elif points >= 85:
  print(5)
