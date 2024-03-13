import smtplib


# f = "rxyj kbrl tnnj gapl"
# smtplib.SMTP("smtp.gmail.com", port=587)

my_email = "queents3@gmail.com"
password = "rxyjkbrltnnjfgearpil" #remove name to work


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

# Define your email content
from_email = my_email
to_email = "queents4@gmail.com"
subject = "Subject"
message = "Hello, this is a test email."

email_content = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{message}"

# first way
connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=email_content)

# second way
# connection.sendmail(from_addr=my_email, to_addrs="queents.queents4@gmail.com", msg=email_content)

connection.quit()
