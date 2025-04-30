 #Boards (création, suppression, listing)
home = {}

def create_boards():
    name = input("name of the board you want to create")
    home = {name:{}}
    return


def sup_boards():
    name = input("name of the board you want to delete")
    del home[name]
    return 

create_boards()
print(home)
sup_boards()
print(home)


# Le projet suiavnt consiste à développer un mini-Trello en ligne de commande, entièrement basé sur des fonctions et sans recours à la POO, afin de familiariser un groupe de trois apprenants Python avec un véritable workflow Git (Git Flow). Les données seront stockées dans un unique fichier JSON (data.json) : on y gère des « boards », chaque board contenant plusieurs « lists » (colonnes) et chaque list une collection de « cards » (éléments). Les apprenants travailleront en parallèle sur trois modules distincts :
    
# Boards (création, suppression, listing)
# Lists (ajout, suppression, listing au sein d’un board)
# Cards (ajout, suppression, déplacement entre lists, listing)

# Chaque module est développé dans une branche feature/..., puis fusionné dans develop après revue de code par un pair.

# En cas de questions, pensez à m'appeler ! (Que ce soit sur le sujet, ou sur les technos utilisées) 
