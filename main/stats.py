# stats.py

def display_bar_statistics(cocktails_db):
    """
    Calculates and displays statistics about the cocktails in memory.
    Requirements: Summary/Status overview.
    """
    print("\n" + "=" * 30)
    print("       BAR STATISTICS")
    print("=" * 30)

    total_cocktails = 0
    custom_cocktails = 0
    all_names = []

    # Перебор категорий (Vodka, Gin и т.д.) и списков коктейлей в них
    for category, list_of_cocktails in cocktails_db.items():
        category_count = len(list_of_cocktails)
        total_cocktails += category_count

        print(f"{category}: {category_count} recipe(s)")

        # Вложенный цикл для подсчета авторских коктейлей и сбора имен
        for cocktail in list_of_cocktails:
            all_names.append(cocktail["name"])
            if cocktail.get("custom") == True:
                custom_cocktails += 1

    print("-" * 30)
    print(f"Total recipes in bar: {total_cocktails}")
    print(f"Author's (Custom) recipes: {custom_cocktails}")
    print(f"Classic recipes: {total_cocktails - custom_cocktails}")

    # Вывод всех названий списком (используем join из Урока 3)
    if all_names:
        print("\nAll cocktail names:")
        print(", ".join(all_names))
    else:
        print("\nThe bar is currently empty.")

    print("=" * 30)


def show_all_recipes(db):
    return None


def display_stats(db):
    return None