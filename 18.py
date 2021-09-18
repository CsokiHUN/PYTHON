def summary(num1, num2):
  counter = 0
  for i in range(num1, num2):
    counter += i
  return counter

print(summary(1, 3))
print(summary(1, 10))