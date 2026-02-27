# 00_cteni_souboru_radek_po_radku.py reseni
# autor reseni: Jan Hruza
# datum: 2026-02-20

def main():
    """
    Opens 'data.txt', reads it line by line, and prints each line with its number.
    Handles FileNotFoundError if 'data.txt' does not exist.
    """
    # Implementujte logiku pro otevření souboru 'data.txt',
    # přečtení jeho obsahu řádek po řádku a vypsání každého řádku s jeho číslem.
    # Formát výpisu je "číslo_řádku: obsah_řádku". Číslování začíná od 1.
    # Pokud soubor není nalezen, vypište chybovou zprávu "Soubor 'data.txt' nebyl nalezen.".
    try:
        with open('data.txt', 'r') as file:
            for line_num, line in enumerate(file, 1):
                print(f"{line_num}: {line.strip()}")
    except FileNotFoundError:
        print("Soubor 'data.txt' nebyl nalezen.")

if __name__ == "__main__":
    main()
