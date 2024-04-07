class MyClass:
	language = "python"
	version = "3.3"

x_obj = getattr(MyClass, "lang", "version")
print(f"x_obj {x_obj}")

f = setattr(MyClass, "language", "python3.12")
x = MyClass.language = "python3.12"

n = MyClass.version = "3.11"
print(f"new version : {n}")
print(f"f print: {f}")
print(f"x object: {x}")

delattr(MyClass, "language")
# or
del MyClass.version


print(f"F after delete language {f}")
print(f"x_obj after removed version: {x_obj}")
########################################################################################################################
class MyClass:
	lang = "python"
	version = "3.3"

attributes = ["lang", "version"]

for attribute in attributes:
	x_obj = getattr(MyClass, attribute, None)
	print(f"{attribute}: {x_obj}")

########################################################################################################################
# get all attributes from a class

class MyClass2:
	lang1 = "python"
	lang2= "ruby"
	lang3 = "java"
	version1 = "3.1"
	version2 = "3.2"
	version3 = "3.3"

all_attributes = vars(MyClass2)
print(f"get all attributes with vars(MyClass): {all_attributes}")


class MyClass3:
	lang1 = "python"
	lang2 = "ruby"
	lang3 = "java"
	version1 = "3.1"
	version2 = "3.2"
	version3 = "3.3"

all_attributes = MyClass3.__dict__
print(f"get all attributes with MyClass.__dict__: {all_attributes}")