# This is where you input your credit card details. It returns it too.
cardnum = str(input("Please input your credit card number."))
print(f"Your card number is {cardnum}. Now processing validity.")

# This is where the credit card is seperated from the checking digit, while saving it and printing it for debug.
cardnumstrip = cardnum[0:15]
checkingdigit = int(cardnum[15:])

# Reverse the remaining digits and define checksum value.
cardnumstrip = cardnumstrip[::-1]
checksumval = 0

# Double digits at even indices.
for x in cardnumstrip[::2]:
  doubleint = int(x) * 2
  if doubleint > 9:
    doubleint += -9
  checksumval += doubleint


for x in cardnumstrip[1::2]:
  checksumval += int(x)
  
checksumval += checkingdigit
if checksumval%10 == 0:
  print("Your credit card number is valid.")
else:
  print("Your credit card number is invalid.")
