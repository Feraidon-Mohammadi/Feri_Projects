class Robot:
    def __init__(self, vor_name, nach_name, age):
        self.vor_name = vor_name
        self.nach_name = nach_name
        self.age = age

    def intrudius(self):
        self.vor_name = str(input("Vor Name :"))
        self.nach_name = str(input("Nach Name: "))
        self.age = int(input("Age: "))

        # don't need it  here an instance
        # r1 = Robot(self.name_s, self.nach_name_s, self.age_int)

    def display_info(self):
        print(f"Vor Name: {self.vor_name}")
        print(f"Nach Name: {self.nach_name}")
        print(f"age: {self.age}")




if __name__ == "__main__":
    robot1 = Robot("", "", 0) # instance Class
    robot1.intrudius()
    robot1.display_info()
