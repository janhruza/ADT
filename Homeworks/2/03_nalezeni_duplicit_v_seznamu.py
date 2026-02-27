# 03_nalezeni_duplicit_v_seznamu.py reseni
# autor reseni: Jan Hruza
# datum: 2026-02-27

def find_duplicates(data: list[int]) -> set[int]:
    """
    Finds duplicate elements in a list of integers.

    Args:
        data (list[int]): List of integers.

    Returns:
        set[int]: Set containing duplicate elements.
    """
    # Vytvořte dvě množiny: jednu pro sledování již viděných čísel
    # a druhou pro ukládání nalezených duplicit.
    # Projděte vstupní seznam a pro každé číslo zkontrolujte,
    # zda jste ho již viděli. Pokud ano, přidejte ho do množiny duplicit.
    # V opačném případě ho přidejte do množiny viděných čísel.
    # Na konci vraťte množinu duplicit.

    # Implementujte logiku pro nalezení duplicit.
    seen = set()
    duplicates = set()

    # Projděte vstupní seznam a pro každé číslo zkontrolujte,
    # zda jste ho již viděli. Pokud ano, přidejte ho do množiny duplicit.
    # V opačném případě ho přidejte do množiny viděných čísel.
    for num in data:
        if num in seen:
            # Pokud ano, přidejte ho do množiny duplicit.
            duplicates.add(num)
        else:
            # V opačném případě ho přidejte do množiny viděných čísel.
            seen.add(num)

    # Vrátěte množinu duplicit.
    return duplicates

def demonstrate_find_duplicates(test_list: list[int]):
    """
    Runs the find_duplicates function on a list and prints the result.
    """
    print(f"Původní seznam: {test_list}")
    duplicates = find_duplicates(test_list)
    print(f"Nalezené duplicity: {duplicates}")
    print("-" * 20)

def main():
    """
    Main function for demonstrating duplicate finding.
    """
    demonstrate_find_duplicates([1, 2, 3, 4, 2, 5, 6, 3])
    demonstrate_find_duplicates([10, 20, 30, 40, 50])
    demonstrate_find_duplicates([])

main()
