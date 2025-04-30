from config import load_data, save_data
data = load_data()
from List import ajout_list,sup_list,listing
from cards_new import ajout_cards, sup_cards,listing_cards,move_card
from board import create_board, delete_board, list_boards

create_board(data,"BOARD TESTFINAL")
ajout_list(data,"BOARD TESTFINAL",'Projet TESTFINAL')
ajout_cards(data,"BOARD TESTFINAL",'Projet TESTFINAL','CARD TESTFINAL','DESCRIPTION DE LA CARD TESTFINAL')
print(data)

# # sup_list(data,'boards','Projet Y')
# # ajout_list(data,'boards','Projet Z')
# # listing(data,"BOARDS_TEST")

# # ajout_cards(data,'boards','Projet Z','CARD Y','DESCRIPTION DE LA CARD Y')
# # ajout_cards(data,'boards','Projet Z','CARD Z','DESCRIPTION DE LA CARD Z')
# # sup_cards(data,'boards','Projet Z','CARD X','DESCRIPTION DE LA CARD X')
# # listing_cards(data,'boards','Projet Z')

# # data[0]['boards']
# print(data["BOARDS_TEST"])