import json
import os
# NEED LATER, PLAYER API: https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=teaxthree

class Fishing:
    def __init__(self, rate=None, amount=None, id=None, location=None, price=None, level=None, members=None):
        self.amount = amount # Fish caught per hour
        self.id = id
        self.location = location
        self.price = price # Low price from API
        self.level = level
        self.members = members
        self.rate = rate

def gpPerHour(amount, price):
    tax = (amount * price) * .01
    return (amount * price) - tax

def getExpRate(amount, fish_id):
    # Match the OSRS fish IDs to their experience rates
    match fish_id:
        case 317:  # Shrimp
            experience_rate = 10
        case 319:  # Anchovies
            experience_rate = 40
        case 333:  # Trout
            experience_rate = 50
        case 329:  # Salmon
            experience_rate = 70
        case 377:  # Lobster
            experience_rate = 90
        case 371:  # Swordfish
            experience_rate = 100
        case 383:  # Shark
            experience_rate = 110
        case _:  # Default case
            experience_rate = 0  # Invalid or unknown fish ID
    
    return experience_rate

#high, highTime, low, lowTime

# Path to the JSON file
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data', 'gp_data.json')

# Load the JSON file
with open(data_file_path, 'r') as file:
    data = json.load(file)


# base - amount fished at starting level
# rate - amount of fish added per level
 
# -- LOBSTER
# -- -- Musa Point
lobster_data = data.get('377', None)
lobster_musaPoint = Fishing(price=lobster_data[2], id=377, level=40, base=180, rate=2.2, location="musa point", members=True) #330 max amount

# -- MONKFISH
# -- -- Fishing Colony
monkfish_data = data.get('7944', None)
monkfish_fishingColony = Fishing(price=monkfish_data[2], id=7944, level=62, base=205, rate=4.59, location="fishing colony", members=True) #375 max amount

# -- SHARK
# -- Location - best is fishing guild
shark_data = data.get('383', None)
shark_fishingGuild = Fishing(price=shark_data[2], id=383, level=76, base=90, rate=3.48, location="fishing guild", members=True) #170 max amount
