def wrapper(s):
  for i in s.split(' '):
    print(i[::-1])

wrapper('teszt szöveg hello')
print()
wrapper('hello')