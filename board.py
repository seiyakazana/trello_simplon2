from config import *

lists_boards1 = data["boards"][0]["lists"]
lists_boards2 = data["boards2"][0]["lists"]

boards1_name = data["boards"][0]["name"]
#print(boards1_name)
#print(lists_boards1)

boards2_name = data["boards2"][0]["name"]
#print(boards2_name)
#print(lists_boards2)

#print(data["boards2"][0]["lists"][0])

board_name = data['boards']

def list_boards():
    if not data["boards"]:
        print("Aucun board trouvé.")
        return
    for key in data.items():
        print(key)

def create_board(board_name):
    if any(board["name"] == board_name for board in data["boards"]):
        print("board déjà existant")
        return
    data["boards"].append({"name": board_name, "lists": []})
    write_data(data)
    print(f"Board '{board_name}' créé")


def delete_board(board_name):
    count = len(data["boards"])
    if len(data["boards"]) < count:
        write_data(data)
        print(f"Board '{board_name}' supprimé.")
    else:
        print(f"Aucun board nommé '{board_name}' trouvé.")


list_boards()
#create_board(board_name)
delete_board(board_name)