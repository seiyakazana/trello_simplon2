 #Boards (création, suppression, listing)
home = {}

def create_boards():
    name = input("name of the board you want to create")
    home = {name:{}}
    return


def sup_boards():
    name = input("name of the board you want to delete")
    del home[name]
    return 

create_boards()
print(home)
sup_boards()
print(home)