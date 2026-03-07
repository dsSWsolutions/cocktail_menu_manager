

import json


def load_data(filename="cocktail_menu_data.json"):
    """Loads cocktails from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty database.")
        return {"Vodka": [], "Gin": [], "Rum": [], "Tequila": [], "Wine": [], "Non-Alcoholic": []}


def save_data(cocktails_db):
    """Saves database to JSON with a filter option."""
    filename = input("Enter filename to save (e.g., my_bar.json): ")
    if not filename.endswith('.json'): filename += '.json'

    print("\n1. Save All\n2. Filter by Category")
    choice = input("Choice: ")

    data_to_save = cocktails_db
    if choice == "2":
        categories = list(cocktails_db.keys())
        for i, cat in enumerate(categories): print(f"{i + 1}. {cat}")
        try:
            idx = int(input("Select category index: ")) - 1
            cat = categories[idx]
            data_to_save = {cat: cocktails_db[cat]}
        except:
            print("Invalid index. Saving all.")

    with open(filename, 'w') as file:
        json.dump(data_to_save, file, indent=4)
    print(f"Data saved to {filename}")