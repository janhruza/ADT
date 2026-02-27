# Vyplneny ukol z 2. cviceni KIV/ADT
# Autor reseni: Jan Hruza
# Datum: 2026-02-27

from dataclasses import dataclass

# Testovací data: Jméno, Osobní číslo, Předmět
# Takto vypadají data načtená například z CSV souboru nebo databáze.
raw_data = [
    ("Jan Novák", "A01N001", "Matematika"),
    ("Petr Svoboda", "A01N002", "Fyzika"),
    ("Jan Novák", "A01N001", "Fyzika"),
    ("Marie Dvořáková", "A01N003", "Informatika"),
    ("Petr Svoboda", "A01N002", "Matematika"),
    ("Jana Černá", "A01N004", "Matematika"),
    ("Karel Nový", "A01N005", "Angličtina"),
    ("Marie Dvořáková", "A01N003", "Angličtina"),
]

@dataclass(frozen=True)
class Student:
    name: str
    os_cislo: str

def get_unique_subjects(data: list[tuple[str, str, str]]) -> set[str]:
    """
    Vrátí množinu unikátních předmětů.
    """
    
    # Vytvoříme množinu
    subjects = set()
    
    # Pro každý záznam v data
    for _, _, subject in data:
        subjects.add(subject)

    return subjects

def group_students_by_subject(data: list[tuple[str, str, str]]) -> dict[str, list[Student]]:
    """
    Vrátí slovník, kde klíčem je předmět a hodnotou seznam studentů (instancí třídy Student),
    kteří jsou na předmět zapsáni.
    """

    # Vytvoříme slovník
    by_subject = {}
    
    # Pro každý záznam v data
    for name, os_cislo, subject in data:
        student = Student(name, os_cislo)
        
        # Pokud předmět není v slovníku, vytvoříme ho
        if subject not in by_subject:
            by_subject[subject] = []
        
        # Přidáme studenta do seznamu
        by_subject[subject].append(student)

    return by_subject

def get_unique_students(data: list[tuple[str, str, str]]) -> set[Student]:
    """
    Vrátí množinu unikátních studentů.
    Pozor: Data obsahují duplicity (jeden student může mít více předmětů).
    Cílem je získat množinu fyzických osob.
    """
    
    # Vytvoříme množinu
    unique_students = set()
    
    # Pro každý záznam v data
    for name, os_cislo, _ in data:
        # Vytvoříme studenta
        student = Student(name, os_cislo)
        
        # Přidáme studenta do množiny
        unique_students.add(student)

    # Vrátíme množinu unikátních studentů
    return unique_students

def get_histogram(data: list[tuple[str, str, str]]) -> dict[str, int]:
    """
    Vrátí histogram, kde klíčem je předmět a hodnotou počet studentů na předmět zapsaných.
    """
    
    # Vytvoříme histogram
    histogram = {}
    
    # Pro každý záznam v data
    for _, _, subject in data:
        # Pokud předmět není v histogramu, vytvoříme ho
        if subject not in histogram:
            histogram[subject] = 0
        
        # Přidáme studenta do histogramu
        histogram[subject] += 1

    # Vrátíme histogram
    return histogram

def get_most_popular_subjects(data: list[tuple[str, str, str]]) -> (str, str):
    """
    Vrátí dvojici nejpopulárnějších předmětů.
    """

    # Vytvoříme histogram
    histogram = get_histogram(data)
    
    # Seřadíme histogram podle počtu studentů (v obráceném pořadí)
    # lambda x: x[1] znamená, že seřadíme podle druhého prvků v tuple (počet studentů)
    # reverse=True znamená, že seřadíme v obráceném pořadí
    sorted_histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    
    # Vrátíme dvojici nejpopulárnějších předmětů
    # sorted_histogram[0][0] je první prvek prvního tuple (nejpopulárnější předmět)
    # sorted_histogram[1][0] je první prvek druhého tuple (druhý nejpopulárnější předmět)
    return sorted_histogram[0][0], sorted_histogram[1][0]

def main() -> None:
    print("--- ÚKOL 1: Unikátní předměty ---")
    subjects = get_unique_subjects(raw_data)
    print(f"Nalezené předměty: {subjects}")

    print("\n--- ÚKOL 2: Studenti dle předmětů ---")
    by_subject = group_students_by_subject(raw_data)
    for subject, students in by_subject.items():
        print(f"{subject}: {len(students)} studentů")
        # print(f"  {students}") # Pro detailní výpis

    print("\n--- ÚKOL 3: Unikátní studenti (Množina) ---")
    unique_students = get_unique_students(raw_data)
    print(f"Počet unikátních studentů: {len(unique_students)}")
    print(unique_students)

    print("\n--- ÚKOL 4: Histogram předmětů ---")
    histogram = get_histogram(raw_data)
    print(f"Histogram předmětů: {histogram}")

    # Kontrola správnosti implementace __eq__ a __hash__
    # V raw_data je 8 záznamů, ale jen 5 unikátních studentů (A101, A102, A103, A104, A105)
    expected_count = 5
    if len(unique_students) == expected_count:
        print(f"\n[OK] Počet studentů odpovídá očekávání ({expected_count}).")
    else:
        print(f"\n[CHYBA] Očekáváno {expected_count} studentů, nalezeno {len(unique_students)}.")
        print("Tip: Funguje správně porovnávání instancí třídy Student v množině?")

    print("\n--- ÚKOL 5: Nejpopulárnější předměty ---")
    most_popular = get_most_popular_subjects(raw_data)
    print(f"Nejpopulárnější předměty: {most_popular}")

if __name__ == "__main__":
    main()
