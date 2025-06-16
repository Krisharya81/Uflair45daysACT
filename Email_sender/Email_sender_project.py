import smtplib
try:
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.starttls()

    ##recevier email
    receiver_email = input("Enter the receiver email: ")

    #mail credentials
    sender_email = "krisharya1911@gmail.com"
    password = "mqkk mmjl altv khea"

    #login to the server
    server.login(sender_email, password)

    #sending email
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")   
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully")

    server.quit()
except Exception as e:
    print("An error occurred:", e)
