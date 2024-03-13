class User:
    pass


user_1 = User() # an object
user_1.id = "002"  # an attribute is a variable associated with object
user_1.username = "Feri" # an attribute is a variable associated with object


class Functions:
    def do_somthing(self):  # a function
        pass

    def __init__(self): # a special function it called => constructor
        pass


class Second:
    def __init__(self, feri, username):  # a special function it called => constructor
        self.name = feri
        # f3f
        self.username = username


# instead of __init__() we can use that , but it is not so good
user_2 = Second()
user_2.name = "feri"  # ==> self.name = feri
print(user_2)


class Third:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # for attribute like this  don't need to add in parameters and it will be default (0)







# question_bank1 = [
#     {question_data[0][0]: question_data[0][1]},
#     {question_data[1][0]: question_data[1][1]},
#     {question_data[2][0]: question_data[2][1]},
#     {question_data[3][0]: question_data[3][1]},
#     {question_data[4][0]: question_data[4][1]},
#     {question_data[5][0]: question_data[5][1]},
#     {question_data[6][0]: question_data[6][1]},
#     {question_data[7][0]: question_data[7][1]},
#     {question_data[8][0]: question_data[8][1]},
#     {question_data[9][0]: question_data[9][1]},
#     {question_data[10][0]: question_data[10][1]},
#     {question_data[11][0]: question_data[11][1]},
# ]

