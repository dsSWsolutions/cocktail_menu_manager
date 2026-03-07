# cocktail_logic.py

def edit_cocktail(cocktails_db):
    """
    Menu to update proportions or remove ingredients.
    Requirement: Maintain minimum 2 ingredients.
    """
    print("\n--- Edit Recipe ---")

    # 1. Select Category
    categories = list(cocktails_db.keys())
    for i, cat in enumerate(categories):
        print(f"{i + 1}. {cat}")

    try:
        cat_choice = int(input("Select category number: ")) - 1
        category = categories[cat_choice]
    except (ValueError, IndexError):
        print("Invalid category.")
        return cocktails_db

    if not cocktails_db[category]:
        print(f"No cocktails found in {category}.")
        return cocktails_db

    # 2. Select Cocktail
    print(f"\nCocktails in {category}:")
    for i, cocktail in enumerate(cocktails_db[category]):
        print(f"{i + 1}. {cocktail['name']}")

    try:
        cocktail_index = int(input("Select cocktail to edit: ")) - 1
        target = cocktails_db[category][cocktail_index]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return cocktails_db

    # 3. Edit Sub-menu
    while True:
        print(f"\nEditing: {target['name']}")
        print("Current ingredients:", target['ingredients'])
        print("1. Change proportion")
        print("2. Remove ingredient")
        print("0. Back to main menu")

        mode = input("Select action: ")

        if mode == "1":
            # Change Proportion
            ing_list = list(target['ingredients'].keys())
            for i, ing in enumerate(ing_list):
                print(f"{i + 1}. {ing}: {target['ingredients'][ing]}")

            try:
                ing_choice = int(input("Select ingredient to change: ")) - 1
                ing_name = ing_list[ing_choice]
                new_amount = float(input(f"Enter new amount for {ing_name}: "))
                target['ingredients'][ing_name] = new_amount
                print("Proportions updated!")
            except (ValueError, IndexError):
                print("Error: Invalid input.")

        elif mode == "2":
            # Remove Ingredient
            if len(target['ingredients']) <= 2:
                print("Error: Cannot remove! A cocktail must have at least 2 ingredients.")
                continue

            ing_list = list(target['ingredients'].keys())
            for i, ing in enumerate(ing_list):
                print(f"{i + 1}. {ing}")

            try:
                ing_choice = int(input("Select ingredient to remove: ")) - 1
                ing_name = ing_list[ing_choice]
                del target['ingredients'][ing_name]  # Удаление ключа из словаря (Урок 4)
                print(f"Removed {ing_name}.")
            except (ValueError, IndexError):
                print("Error: Invalid selection.")

        elif mode == "0":
            break
        else:
            print("Invalid option.")

    return cocktails_db


def add_cocktail(db):
    return None


def search_ingredient(db):
    return None