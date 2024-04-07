import prettytable
#from prettytable import PrettyTable

my_table = prettytable.PrettyTable()
pockemon = ["Roy", "Megan","Anna", "Rock","jessy", "Taniya","Twist", "Ritta"]
skill = ["kamper", "rusher","worker", "starter","cleaner", "roman","creator", "singer"]

data = my_table.add_column("Pockemon", pockemon)
date2 = my_table.add_column("type",skill)
date3 = my_table.add_column("Numbers", ["one", "two","three", "four","five", "six","seven", "eight"])
my_table.align = "l"

print(my_table)


