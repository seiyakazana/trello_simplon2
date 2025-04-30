from config import load_data, save_data
data = load_data()

def list_boards():
    """"""
    data = load_data()
    if not data["boards"]:
        print("Aucun board trouvé.")
        return
    for key in data:
        print(key)

def create_board(data, board_name):
    data = load_data()
    if any(board["name"] == board_name for board in data["boards"]):
        print(f"Le board '{board_name}' existe déjà.")
        return
    new_board = {board_name : []}
    data.update(new_board)
    save_data(data)
    print(f"Board '{board_name}' créé avec succès.")
    return data

def delete_board(board_name):
    data = load_data()
    for board in data:
        if board == board_name:
            data.pop(board)
            save_data(data)
            print(f"Board '{board_name}' supprimé.")
            return
    print(f"Aucun board nommé '{board_name}' trouvé.")


#create_board(data, 'boards2')
#delete_board('boards2')
list_boards()