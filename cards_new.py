# Cards (ajout, suppression, déplacement entre lists, listing)

from config import data

def ajout_cards(board,list_name,cards_name,text_card):
    for i in range(len(data[board])):
        if data[board][i]["name"] == list_name:
            data[board][i]["lists"].append({'name': cards_name, 'cards': text_card})

def sup_cards(board,list_name,cards_name):
    for i in range(len(data[board])):
        if data[board][i]["name"] == list_name:
            for j in range(len(data[board][i]["lists"])):
                        if data[board][i]["lists"][j]['name'] == cards_name:
                            del data[board][i]["lists"][j]


def listing_cards(board,list_name):
    for i in range(len(data[board])):
            if data[board][i]["name"] == list_name:
                for j in range(len(data[board][i]["lists"])):
                    print(data[board][i]["lists"][j]['name'])


def move_card(board,list_name1,list_name2,card_name):
    for i in range(len(data[board])):
                if data[board][i]["name"] == list_name1:
                    for j in range(len(data[board][i]["lists"])):
                        if data[board][i]["lists"][j]['name'] == card_name:
                            data_card = data[board][i]["lists"][j] 
                            del data[board][i]["lists"][j]
                if data[board][i]["name"] == list_name2:
                    data[board][i]["lists"].append(data_card)
                        


#TEST

ajout_cards("boards","Projet X",'TO DO', 'task to do...........')
ajout_cards("boards","Projet X",'TO DO2', 'task to do...........')
sup_cards("boards","Projet X",'TO DO')
listing_cards("boards","Projet X")