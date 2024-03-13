"""
Exercise 1: Create a Person Class
Create a Person class with the following attributes: name, age, and gender.
Implement a method called introduce that prints a greeting including the person's name, age, and gender.
"""


"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        name = self.name = str(input(f"Register form \n\nEnter your Name: ")).strip()
        age = self.age = int(input(f"Enter your Age: "))
        gender = str(input(f"Gender F for female and M for Male: ")).strip().lower()

        if gender == "F".lower() or gender == "female".lower():
            self.gender = "Female"
        elif gender == "M".lower() or gender == "male".lower():
            self.gender = "Male"

        f = f"\nGreeting user. \nName: {name} \nGender: {self.gender} \nAge: {age} years old \n"
        return f


instance_obj = Person(age="Age", name="Name", gender="Gender")
f = instance_obj.introduce()

print(f)

# #################################### gpt fixed:####################################
class Person:
    def __init__(self):
        self.name = input("Enter your Name: ").strip()
        self.age = int(input("Enter your Age: "))
        gender_input = input("Gender F for female and M for Male: ").strip().lower()

        if gender_input == "f" or gender_input == "female":
            self.gender = "Female"
        elif gender_input == "m" or gender_input == "male":
            self.gender = "Male"
        else:
            self.gender = "Unknown"

    def introduce(self):
        info = f"\nGreeting user. \nName: {self.name} \nGender: {self.gender} \nAge: {self.age} years old \n"
        return info


# Example usage:
instance_obj = Person()
output = instance_obj.introduce()
print(output)

"""


########################################################### completed  ###################################################

class Person1:
    def __init__(self, name: str, age: int, gender:str)-> None:
        self.name = name  # str(input(f"Register form \n\nEnter your Name: ")).strip()
        self.age = age  # int(input(f"Enter your Age: "))
        self.gender = gender.lower()  # str(input(f"Gender F for female and M for Male: ")).strip().lower()

    def introduce(self)->str:

        if self.gender == "F".lower() or self.gender == "female".lower():
            self.gender = "Female"
        elif self.gender == "M".lower() or self.gender == "male".lower():
            self.gender = "Male"
        else:
            self.gender = "unknown"



        get_info = f"\nGreeting user. \nName: {self.name} \nGender: {self.gender} \nAge: {self.age} years old \n"
        return get_info


instance_obj = Person1(age=3, name="Ali", gender="f")
f = instance_obj.introduce()

print(f)
