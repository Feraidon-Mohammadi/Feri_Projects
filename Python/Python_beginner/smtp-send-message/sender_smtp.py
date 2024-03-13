import smtplib


#f = "rxyj kbrl tnnj gapl"
#smtplib.SMTP("smtp.gmail.com", port=587)

my_email = "33333@gmail.com"
password = "rxyjkbrltnnjfgearpil" # remove your name to get the pass


"""
# how is smtplib created , its the example how did it
class SMTP1:
	
	def smtplib(self, str):
		return str
	
	def start(self):
		pass
	
	def login(self, key :value , password:value )
		pass
		
	def sendmail(self, from_addr="", to_addrs="", msg="" )
		pass
		
	def quit(self)
		pass
		
SMTP =  SMTP1()
smtplib.SMTP("smtp.gmail.com")

"""




connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

# Define your email content
from_email = my_email
to_email = "44444@gmail.com"
subject = "Subject"
message = "Hello, this is a test email."

email_content = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{message}"

# first way
connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=email_content)

# second way
# connection.sendmail(from_addr=my_email, to_addrs="4444@gmail.com", msg=email_content)

connection.quit()
