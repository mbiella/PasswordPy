import smtplib

def sendEmail(message, dest):
    oggetto = "Subject: Nuova password!\n\n"
    contenuto = "Buongiorno/Buonasera, in allegato si invia la password generata: " + message
    messaggio = oggetto + contenuto
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login("maurizio.biella.python", "python2022")
    email.sendmail("maurizio.biella.python@gmail.com", dest, messaggio)
    email.quit()
    print("Mail sent!")