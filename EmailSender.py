import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = input("Email: ")
password = input("Password: ")
message =input("Message: ")
receiver_email =input("Send to: ")
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: szabo.martin.mate.github@gmail.com
    server.sendmail(sender_email, receiver_email, message)

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()