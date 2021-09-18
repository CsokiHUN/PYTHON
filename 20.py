def symbols(num):
  for i in range(num):
    print((i + 1) % 3 == 0 and '+' or '-')

symbols(10)