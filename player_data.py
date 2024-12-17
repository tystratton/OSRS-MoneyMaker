import requests
import json
import os

def fetch_player():
    name = input("What is your character's name? ").replace(" ", "_")  # Replace spaces with underscores
    endpoint_url = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=' + name
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        # The API returns raw text, not JSON
        lines = response.text.strip().split("\n")
        skills = [
            "Overall", "Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer", "Magic",
            "Cooking", "Woodcutting", "Fletching", "Fishing", "Construction", "Crafting", "Smithing",
            "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecraft", "Hunter"
        ]

        # Parse and map the data
        player_data = {}
        for i, line in enumerate(lines):
            values = line.split(",")
            if len(values) == 3:  # Only process valid lines
                rank, level, xp = map(int, values)  # Correct order: Rank, Level, XP
                if i < len(skills):  # Ensure we don't exceed the skills list
                    player_data[skills[i]] = {"Rank": rank, "Level": level, "XP": xp}

        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(script_dir, 'data', 'player_data.json')

        # Save to JSON file in the 'data' folder
        with open(data_file_path, "w") as file:
            json.dump(player_data, file, indent=4)

        print("Player data saved to 'data/player_data.json'")
    else:
        print(f"Error: Failed to fetch data for '{name}'. Status Code: {response.status_code}")

# Run the function
fetch_player()
