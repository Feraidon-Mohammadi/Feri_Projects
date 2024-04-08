import zipfile


import zipfile

zip_file_path = ".\\Kursmaterialien\\data\\New folder.zip"
extract_to_path = ".\\Kursmaterialien"
zeichens = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456f7e8r9i"

for char in zeichens:
    password = char * 4  # Assuming you want to repeat each character 4 times

    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        try:
            zip_file.extractall(extract_to_path, pwd=password.encode('utf-8'))
            print(f"Extraction successful with password: {password}")
            break  # Stop the loop if a correct password is found
        except zipfile.BadZipFile:
            print(f"Attempted password: {password} - Incorrect password.")


































#
# zip_file_path = ".\\Kursmaterialien\\data\\New folder.7z.rar"
# extract_to_path = ".\\Kursmaterialien"
#
# #password = 'your_password'  # Replace with the correct password
# zeichens = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#
# with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
#
#     for char in zeichens:
#         a = char
#
#
#     try:
#         zip_file.extractall(extract_to_path, pwd=password.encode('utf-8'))
#         print("Extraction successful.")
#     except zipfile.BadZipFile:
#         print("Invalid ZIP file or incorrect password.")
#