a_string = input("Stringa da codificare? ")

ASCII_values = []

for char in a_string:
    ASCII_values.append(ord(char))

print(ASCII_values)

finalNumb=''

for numb in ASCII_values:
    finalNumb=finalNumb + str(numb)

finalNumb = int(finalNumb)

'''
toHex = []

for digit in ASCII_values:
    toHex.append(hex(digit))

#print(toHex)

finalHex=''

for numb in toHex:
    finalHex=finalHex + numb[2::]

finalHex = '0x' + finalHex
print(finalHex)


'''

key = input("Chiave? ")
print("Chiave ", key)
print("Numero", finalNumb)

pwd = finalNumb * int(key)

#print(pwd)
aa = hex(pwd)
pwd = str(hex(pwd))
pwd = pwd[2::]
print(pwd)
print(int(aa, 16))
