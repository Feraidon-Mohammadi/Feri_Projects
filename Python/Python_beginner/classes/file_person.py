import argparse

class Person:
    def __init__(self, vor_name, nach_name, age):
        self.vor_name = vor_name
        self.nach_name = nach_name
        self.age = age

    def display_info(self):
        print(f"Vor Name: {self.vor_name}")
        print(f"Nach Name: {self.nach_name}")
        print(f"Age: {self.age}")

def main():
    parser = argparse.ArgumentParser(description="Robot Information")
    parser.add_argument("-vn", "--vor_name", required=True, help="Vor Name")
    parser.add_argument("-nn", "--nach_name", required=True, help="Nach Name")
    parser.add_argument("-age", "--age", required=True, type=int, help="Age")

    args = parser.parse_args()

    r = Person(args.vor_name, args.nach_name, args.age)
    r.display_info()

if __name__ == "__main__":
    main()
