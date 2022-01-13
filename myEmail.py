import smtplib

def sendEmail(message):
    oggetto = "Subject: Nuova password!\n\n"
    contenuto = "in allegato la nuova password: " + message
    messaggio = oggetto + contenuto
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login("maurizio.biella.python", "python2022")
    email.sendmail("maurizio.biella.python@gmail.com", "maurizio.biella@gmail.com", messaggio)
    email.quit()
    print("Mail sent!")