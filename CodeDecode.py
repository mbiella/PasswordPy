import myEmail as em

a_string = input("Stringa da codificare? ")

ASCII_values = []

for char in a_string:
    ASCII_values.append(ord(char))

print(ASCII_values)

finalNumb=''

for numb in ASCII_values:
    finalNumb=finalNumb + str(numb)

finalNumb = int(finalNumb)

key = input("Chiave? ")
#print("Chiave ", key)
#print("Numero", finalNumb)

pwd = finalNumb * int(key)

#print(pwd)
pwd = str(hex(pwd))
pwd = pwd[2::]
print("Password generata: ", pwd)
#print(int(aa, 16))
sendMail = input("Vuoi inviare la password per mail s/n? ")

if(sendMail == 's'):
    dest = input("Scrivi il destinatario: ")
    em.sendEmail(pwd, dest)

print("Fine programma")
