print('BANK OF CODÉDEX')
pin = int(input('Enter your PIN: '))
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')



# Guess Number 🔢
# Codédex

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number:  '))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')