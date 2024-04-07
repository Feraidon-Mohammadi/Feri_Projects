from data_flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask World!'

# self added method to run trough / in link
@app.route("/feri")
def feri_decoratro():
    return "Welcome to feri Page"

# if runing without this debug  , dann need to set the activate and run flask from terminal to do that .do following step
#1 # set FLASK_APP=your_module_name.py
#2 # flask run

if __name__ == '__main__': # run without this 2 lines , then follow upper 2 steps
    app.run(debug=True)