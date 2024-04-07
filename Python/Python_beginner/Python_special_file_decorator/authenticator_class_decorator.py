

class User_log_data:
	def __init__(self, name):
		self.name = name
		self.is_loged_in = False
		
		
def is_authenticated_decorator(function):
	def wrapper(*args, **kwargs):
		if args[0].is_loged_in == True:
			function(args[0])
	return wrapper

@is_authenticated_decorator
def create_blog_post(user):
	print(f"this is {user.name}'s new blog post.")
	
new_user = User_log_data("feri")
new_user.is_loged_in = True
create_blog_post(new_user)


