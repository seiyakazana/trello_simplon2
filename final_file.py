from config import load_data, save_data
data = load_data()
from List import ajout_list,sup_list,listing
from cards_new import ajout_cards, sup_cards,listing_cards,move_card

data.update({"BOARDS_TEST":[]})



ajout_list(data,"BOARDS_TEST",'Projet Y')
# sup_list(data,'boards','Projet Y')
# ajout_list(data,'boards','Projet Z')
# listing(data,"BOARDS_TEST")
ajout_cards(data,"BOARDS_TEST",'Projet Y','CARD X','DESCRIPTION DE LA CARD X')
# ajout_cards(data,'boards','Projet Z','CARD Y','DESCRIPTION DE LA CARD Y')
# ajout_cards(data,'boards','Projet Z','CARD Z','DESCRIPTION DE LA CARD Z')
# sup_cards(data,'boards','Projet Z','CARD X','DESCRIPTION DE LA CARD X')
# listing_cards(data,'boards','Projet Z')

# data[0]['boards']
print(data["BOARDS_TEST"])