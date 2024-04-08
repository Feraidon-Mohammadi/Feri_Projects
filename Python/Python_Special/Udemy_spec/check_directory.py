import os

directory = 'static/'
if os.path.exists(directory):
    print(f"The directory '{directory}' exists.")
else:
    print(f"Directory '{directory}' does not exist.")