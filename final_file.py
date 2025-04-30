from config import load_data, save_data
data = load_data()
from List import ajout_list,sup_list,listing
from cards_new import ajout_cards, sup_cards,listing_cards,move_card

ajout_list(data,'boards','Projet Z')
print(data['boards'])