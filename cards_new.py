# Cards (ajout, suppression, déplacement entre lists, listing)

from config import load_data, save_data
data = load_data()

def ajout_cards(data,board,list_name,cards_name,text_card):
    for i in range(len(data[board])):
        if data[board][i]["name"] == list_name:
            data[board][i]["lists"].append({'name': cards_name, 'cards': text_card})

def sup_cards(data,board,list_name,cards_name,text_card):
    for i in range(len(data[board])):
        if data[board][i]["name"] == list_name:
            data[board][i]["lists"].remove({'name': cards_name, 'cards': text_card})


def listing_cards(data,board,list_name):
    for i in range(len(data[board])):
            if data[board][i]["name"] == list_name:
                for j in range(len(data[board][i]["lists"])):
                    print(data[board][i]["lists"][j]['name'])


def move_card(data,board,list_name1,list_name2,card_name):
    for i in range(len(data[board])):
                if data[board][i]["name"] == list_name1:
                    for j in range(len(data[board][i]["lists"])):
                        if data[board][i]["lists"][j]['name'] == card_name:
                            data_card = data[board][i]["lists"][j] 
                            del data[board][i]["lists"][j]
                if data[board][i]["name"] == list_name2:
                    data[board][i]["lists"].append(data_card)
