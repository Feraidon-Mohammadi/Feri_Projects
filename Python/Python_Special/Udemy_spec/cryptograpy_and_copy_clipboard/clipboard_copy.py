import pyperclip

# Copy text to clipboard
pyperclip.copy("Text to be copied")

# Paste text from clipboard
copied_text = pyperclip.paste()

print(copied_text)




#########################  or ###################################

import pyperclip
import time

# Copy password to clipboard
pyperclip.copy("SecurePassword123")

# Wait for a few seconds (configurable based on your security needs)
time.sleep(10)

# Clear the clipboard
pyperclip.copy("")

"""
This helps enhance security by automatically clearing sensitive information from the clipboard after a specified time,
 reducing the risk of exposure if someone gains access to the clipboard contents.


"""