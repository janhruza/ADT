
"""
This module provides functions to manage a dictionary of users.
"""

def add_or_update_user(users: dict, name: str, email: str) -> None:
    """
    Adds a new user to the dictionary or updates an existing user's email.

    Args:
        users (dict): The dictionary of users.
        name (str): The name of the user (key).
        email (str): The email of the user (value).
    """
    # Implementujte logiku pro přidání nebo aktualizaci uživatele.
    users[name] = email
    return users

def check_user_exists(users: dict, name: str) -> bool:
    """
    Checks if a user exists in the dictionary.

    Args:
        users (dict): The dictionary of users.
        name (str): The name of the user to check.

    Returns:
        bool: True if the user exists, False otherwise.
    """
    # Implementujte logiku pro kontrolu existence uživatele.
    return name in users

def main():
    """
    Main function to demonstrate user management.
    """
    user_database = {}
    print(f"Počáteční stav databáze: {user_database}")

    print("\nPřidávám uživatele 'Alice'...")
    add_or_update_user(user_database, "Alice", "alice@example.com")
    print(f"Stav databáze: {user_database}")

    print("\nPřidávám uživatele 'Bob'...")
    add_or_update_user(user_database, "Bob", "bob@example.com")
    print(f"Stav databáze: {user_database}")

    print("\nAktualizuji uživatele 'Alice'...")
    add_or_update_user(user_database, "Alice", "new.alice@example.com")
    print(f"Stav databáze: {user_database}")

    print(f"\nOvěřuji, zda existuje 'Alice': {check_user_exists(user_database, 'Alice')}")
    print(f"Ověřuji, zda existuje 'Charlie': {check_user_exists(user_database, 'Charlie')}")

main()

