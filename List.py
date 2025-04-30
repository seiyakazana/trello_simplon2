# Lists (ajout, suppression, listing au sein d’un board)
from config import data

def ajout_list(board,list_name):
    data[board].append({'name':list_name,'lists':[]})

def sup_list(board,list_name):
    data[board].remove({'name':list_name,'lists':[]})

def listing(board):
    for i in range(len(data[board])):
        print(data[board][i]["name"])

#TEST
ajout_list("boards","PROJET Y")
sup_list("boards","PROJET Y")
ajout_list("boards","PROJET Z")
listing("boards")
print(data['boards'])
