from typing import List, Tuple

def process_file_data(file_path: str) -> List[Tuple[str, str, str]]:
    """
    Reads a file, parses lines for student data, and returns them as a list of tuples.

    Each line is expected to be in the format "name - surname - points".

    Args:
        file_path: The path to the file.

    Returns:
        A list of tuples, where each tuple contains (name, surname, points).
        Returns an empty list if the file is not found or contains no valid data.
    """
    # Implementujte logiku pro čtení souboru a parsování dat.
    # Soubor obsahuje data o studentech ve formátu: jméno - příjmení - body.
    # Funkce by měla vrátit seznam n-tic (jméno, příjmení, body).
    # Řádky, které neodpovídají formátu, ignorujte.
    # Pokud soubor neexistuje, vraťte prázdný seznam.
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('-')
                if len(parts) == 3:
                    name = parts[0].strip()
                    surname = parts[1].strip()
                    points = parts[2].strip()
                    yield (name, surname, points)
    except FileNotFoundError:
        return []

def main():
    """
    Main function to process 'data.txt' and print the student data.
    """
    filepath = "data.txt"
    student_data = process_file_data(filepath)

    if student_data:
        print("Načtená data studentů:")
        for name, surname, points in student_data:
            print(f"{name} {surname}: {points} bodů")
    else:
        print(f"Soubor '{filepath}' nebyl nalezen nebo neobsahuje platná data.")

if __name__ == "__main__":
    main()
