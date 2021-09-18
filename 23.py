nums = []

while True:
  try:
    num = int(input('Adj meg egy számot: '))
    if num < 0:
      continue
    elif num == 0:
      break
    else:
      nums.insert(0, num)
  except:
    continue

for i in nums:
  print(i)