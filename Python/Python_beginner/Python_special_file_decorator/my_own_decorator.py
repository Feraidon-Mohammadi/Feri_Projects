import time


current_time = time.time()

def decorator_fast(function):
	def wrapper():
		start_time = time.time()
		function()
		end_time = time.time()
		print(f"{function.__name__} run speed: {end_time - start_time}a")
	return wrapper







@decorator_fast
def fast_faction():
	for i in range(1000000):
		i * i



@decorator_fast
def slow_fanction():
	for i in range(100000000):
		i*i


fast_faction()
slow_fanction()
