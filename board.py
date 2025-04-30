from config import load_data, save_data
data = load_data()

def list_boards():
    data = load_data()
    if not data["board"]:
        print("Aucun board trouvé.")
        return
    for key in data.items():
        print(key)

def create_board(data, board_name):
    data = load_data()
    if any(board["name"] == board_name for board in data["boards"]):
        print(f"Le board '{board_name}' existe déjà.")
        return
    new_board = {
        board_name : []
    }
    data["board"].append(new_board)
    save_data(data)
    print(f"Board '{board_name}' créé avec succès.")
    return data

def delete_board(board_name):
    data = load_data()
    for board in data["board"]:
        if board["name"] == board_name:
            data["board"].remove(board)
            save_data(data)
            print(f"Board '{board_name}' supprimé.")
            return
    print(f"Aucun board nommé '{board_name}' trouvé.")


create_board(data, 'board test')
#delete_board('board test')
#list_boards()