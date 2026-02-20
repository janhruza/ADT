def parse_personal_data(data_string: str) -> tuple[str, str, int, int, int] | None:
    """
    Parses a string containing personal data in the format "name;surname;day.month.year".

    Args:
        data_string: The string to parse.

    Returns:
        A tuple (name, surname, day, month, year) with integer date parts,
        or None if the format is invalid.
    """
    # Implementujte logiku pro rozdělení řetězce, převod částí data na celá čísla,
    # a extrakci dat.
    # Pokud je formát nesprávný nebo převod selže, vraťte None.

    try:
        name, surname, date = data_string.split(";")
        day, month, year = map(int, date.split("."))
        return name, surname, day, month, year
    except ValueError:
        return None

# Vstupní bod pro demonstraci funkčnosti
if __name__ == "__main__":
    print(parse_personal_data("Jan;Novák;24.12.2020"))
    print(parse_personal_data("Peter;Pan;01.01.1990"))
    print(parse_personal_data("Neplatný;vstup"))
    print(parse_personal_data("Jan;Novák;24-12-2020"))
    print(parse_personal_data("Jan;Novák;den.mesic.rok"))
