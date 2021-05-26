import ezgmail


#Gathering info stuff
mail = input("Enter the email address you want to email: ")
subject = input("What will be the subject?: ")
text = input("And the main body text?: ")


#actually sending mail
print("Sending...")
ezgmail.send(mail, subject, text, mimeSubtype='html')
print("Aaaand... sent!")