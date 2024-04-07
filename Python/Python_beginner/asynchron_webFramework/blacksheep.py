

# python -m venv basic-app
# cd basic-app
# source bin/activate
# pip install blacksheep uvicorn


# BlackSheep can be used to create server-side or full-stack applications with an MVC pattern.
# create a file name : server.py  and use this codes below
from blacksheep import Application

app = Application()

@app.router.get("/")
def home():
    return "Hello, World!"


"""

Project Setup
Let’s create a basic server-side application with BlackSheep. Quickly run the below commands one by one to set up the project.

python -m venv basic-app
cd basic-app
source bin/activate
pip install blacksheep uvicorn
Learn how to install PIP package installer on CentOS, Ubuntu and Windows.

We are done with setting up the project. Let’s create a file called server.py and place the following code.

from blacksheep import Application

app = Application()

@app.router.get("/")
def home():
    return "Hello, World!"
We have created our most famous hello world application. There is only one route with HTTP GET method for now, and it’s /. The function home is called request handler in BlackSheep.

We have used a router decorator from the app. There is another way to create routes i.e.., route. We will be using the router in this tutorial. You can find more about route in the docs.

Let’s run the application with the following command.

uvicorn server:app --port 8000 --reload
Go to the http://localhost:8000/ in the browser. You will see hello world in the browser. Let’s talk a bit about the command that we used to run the application.

We have used uvicorn package to run our application.
The server is the file name that we have given. If you use a different file name, change it in the start command as well.
The option --port is give the port on which our app should run.
Finally, the --reload option is to reload the application in the browser whenever we make changes to the server file.
JSON Response
In the real world, we need the API responses in JSON in most cases. We can return a JSON response from the method by wrapping the JSON object with json from the blacksheep package. Let’s see how we can do it.

from blacksheep import Application, json

app = Application()

@app.router.get("/")
def home():
    return json({"message": "Hello, World!"})
We have imported json from the blacksheep and wrapped the JSON object with it. Check it in the browser for JSON response.

Route Parameters
We need to accept the route params sometimes for the requests. We can do it in BlackSheep by defining them inside the HTTP method. Let’s see it.

@app.router.get("/{name}")
def home(name):
    return json({"greetings": f"Hello, {name}!"})
We are accepting one route parameter called name. Go to the http://localhost:8000/Geekflare. The method will return a greeting with the name given in the route.

The router decorator will pass the parameter with the same name to the home function as it’s given to the decorator. Here, it will be name. If you change it in the decorator, change it in the home function as well.

We can accept as many route parameters as possible in a similar way. Let’s see a quick example.

@app.router.get("/{name}/{info}")
def home(name, info):
    return json({"greetings": f"Hello, {name}! Info {info}"})
We have accepted one more route parameter called info. Go to http://localhost:8000/Geekflare/Chandan to check it.

Query Parameters
We don’t need to do anything to accept the query parameters. BlackSheep will automatically send the query parameters to the function in the form of a list. Let’s see the example.

@app.router.get("/")
def home(name):
    print(name)
    return json({"greetings": f"Hello, {name[0]}!"})
Go to http://localhost:8000/?name=Geekflare to check the response. If you have multiple query parameters with the same name, BlackSheep will add all of them to the list.

Go to http://localhost:8000/?name=Geekflare&name=Chandan and check the output in the terminal. You will see a list with Geekflare and Chadan as we have passed two query parameters with the same name.

If you want multiple query parameters with different, you can do it too. Just add another argument to the function with the query parameter name and do what you want with it.

Request Object
The only thing left in our basics is checking other HTTP methods. Before going into it, let’s check the request object for the API.

All the request handlers in the BalckSheep will have a request argument which contains all the information of the coming request. It includes request headers, path parameters, query parameters, data, etc..,

Let’s see an example to see the request object.

@app.router.post("/")
def home(request):
    print(request)
    return "Hello, World!"
You can see the following output in the terminal.

<Request POST />
We can access different things from the request. You can check the docs for it. Here, our focus is on the request body. Let’s see how to access the request body from the request object.

@app.router.post("/")
async def home(request):
    data = await request.json()
    print(data)
    return "Hello, World!"
There is a method called json in the request, which will return the data that’s coming from the request. Pass some data in the API request and call it. You will see the data printing in the terminal that you have passed to the API.

















"""


