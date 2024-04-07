class Person:
    def __init__(self, name:str, age: str, gender: str)-> None:
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self)-> str:
        name = self.name = str(input(f"Register form \n\nEnter your Name: ")).strip()
        age = self.age = int(input(f"Enter your Age: "))
        gender = str(input(f"Gender F for female and M for Male: ")).strip().lower()

        if gender == "F".lower() or gender == "female".lower():
            self.gender = "Female"
        elif gender == "M".lower() or gender == "male".lower():
            self.gender = "Male"

        f = f"\nGreeting user. \nName: {name} \nAge: {age} years old \nGender: {self.gender} \n"
        return f


instance_obj = Person(age="Age", name="Name", gender="Gender")
f = instance_obj.introduce()

print(f)

