
class Devices:
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name

        result = True
        if result:
            self.status = "Activated"
        else:
            self.status = "Deactivated"


    # an exception falls benutzer eine falsche eingabe eingibt(interger instead of str)
    def functionality(self):
        iplist = []
        user_input = int(input("Give input [ip] or [mac address] or [device name]"))
        if user_input == '_''_''_''_':
            print(f"user eingabe Ip : {user_input}")
        elif user_input == '__''__''__''__''__''__':
            print(f"user eingabe Mac Address: {user_input}")
        elif user_input == "":
            print(f"device name: {self.name}")


        try:
            print(user_input)
        except:
            return str(user_input)


    def display_input(self):
        print(f"user eingabe : {self.ip}")


    def get_status(self):
        print(self.status)
        return self.status

if __name__ =="__main__":
    obj1 = Devices("","","")
    obj1.functionality()
    obj1.display_input()
