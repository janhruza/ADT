# 02_sprava_skladu_s_ovocem.py reseni
# autor reseni: Jan Hruza
# datum: 2026-02-27

def add_fruit(inventory: dict, fruit_name: str, quantity: int) -> dict:
    """
    Adds or updates the quantity of fruit in the warehouse.

    Args:
        inventory: Dictionary representing the warehouse. Keys are fruit names, values are quantities.
        fruit_name: Name of the fruit to add or update.
        quantity: Quantity of fruit to add.

    Returns:
        Updated warehouse dictionary.
    """
    # Check if the fruit already exists in the warehouse (key exists).
    # If yes, add the quantity. If no, create a new entry.

    # Implementujte logiku pro přidání nebo aktualizaci množství ovocí.
    if fruit_name in inventory:
        # Přidání množství ovocí
        inventory[fruit_name] += quantity
    else:
        # Vytvoření nového záznamu
        inventory[fruit_name] = quantity

    # Vrácení aktualizovaného slovníku
    return inventory

def main():
    """
    Main function for warehouse management demonstration.
    """
    fruit_warehouse = {}
    print(f"Počáteční stav skladu: {fruit_warehouse}")

    fruit_warehouse = add_fruit(fruit_warehouse, "apple", 10)
    print(f"Po přidání jablek: {fruit_warehouse}")

    fruit_warehouse = add_fruit(fruit_warehouse, "banana", 5)
    print(f"Po přidání banánů: {fruit_warehouse}")

    fruit_warehouse = add_fruit(fruit_warehouse, "apple", 7)
    print(f"Po dalším přidání jablek: {fruit_warehouse}")

main()
