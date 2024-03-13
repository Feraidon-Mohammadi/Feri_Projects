import random
import smtplib
import datetime as dt

import re

my_email = "333@gmail.com"
password = "rxyjkbrltnnjfgearpil"  # remove your name to get the pass

now = dt.datetime.now()
print(now)

year = now.year
month = now.month
day_of_week = now.weekday()
day_of_week_str = now.strftime("%A")
print(day_of_week)

time_now = now.time()
print(time_now)


birth_day = dt.datetime(year=2023, month=11, day=12, hour=15, minute=11, second=22, microsecond=234)
print(birth_day)

day_name = now.strftime("%A")
print(day_name)


# email = "ff@.com"
# passowr= "ewifjwufpwufhfweirhif"

# obj_connect = smtplib.SMTP(host="feri", port=25, local_hostname="faraidon",timeout=22,source_address=tuple("123.123.123.4"))

def checker():
	my_list = []
	with open("D:\\Visual studio\\fereydoun project\\py_beginner IAD\\Py_beginner\\smtp-send-message\\quotes.txt", "r", encoding="utf-8") as quotes_text:
		content = quotes_text.read()
		contents = content.split("”–")
		for element in contents:
			if year == 2023 and month == 11:
				x = random.choice(element.strip().split("\n"))
				my_list.append(x)
			# print(my_list)
			break
	return my_list
x = checker()
print(x)

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)

from_address = "33333@gmail.com"
to_address = "444444@gmail.com"
subject = "Happy birthday to you :) "
# not need link but I want add
link = "https://youtu.be/ryUxrFUk6MY"

message = f"{x} \n\n\n {link}\n\n\n {day_name}"

# Remove special characters from the message using regex
# message = re.sub(r'[^\x00-\x7F]+', '', message)


contents = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}"

# Encode the email content with UTF-8
contents_encoded = contents.encode('utf-8')

connection.sendmail(from_addr=from_address, to_addrs=to_address, msg=contents_encoded)

connection.quit()




