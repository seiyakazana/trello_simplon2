# Lists (ajout, suppression, listing au sein d’un board)
from config import load_data, save_data
data = load_data()

def ajout_list(board,list_name):
    data[board].append({'name':list_name,'lists':[]})

def sup_list(board,list_name):
    data[board].remove({'name':list_name,'lists':[]})

def listing(board):
    for i in range(len(data[board])):
        print(data[board][i]["name"])