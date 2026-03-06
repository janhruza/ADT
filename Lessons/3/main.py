from collections import defaultdict
import os
import sys
from dataclasses import dataclass

# Dataclass je skvělá volba pro reprezentaci záznamu (Bod 3 zadání).
@dataclass
class Record:
    time: int
    id_cust: int
    # Přidáno kvůli volitelné částce u pokladny, kterou zmiňuje zadání.
    # Výchozí hodnota je 0.0, aby nepadal kód u checkpointů, kde útrata není.
    cost: float = 0.0  

def load_data(data_path: str, city: str, shop: str, day: str = "1-Mon") -> \
        dict[str, list[Record]] | None:
    """ Funkce načte data z daného souboru a vrátí je jako slovník.
    Klíčem je název checkpointu a hodnotou je list záznamů.
    """
    # Použití defaultdict usnadňuje přidávání do seznamů v hodnotách.
    # Pokud klíč (checkpoint) ještě neexistuje, automaticky se vytvoří prázdný list.
    city_data: dict[str, list[Record]] = defaultdict(list)

    print(f"Loading data for {city}, {shop}...")
    
    # os.path.join bezpečně spojí cesty nezávisle na operačním systému (Windows/Linux)
    sDir = os.path.join(data_path, city, day)
    sFile = os.path.join(sDir, f"{shop}.txt")
    
    # Bod 2 zadání: Ověření existence cesty/souboru
    if not os.path.exists(sFile):
        print(f"File not found: {sFile}")
        return None

    with open(sFile, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        # Bod 5.1 zadání: Přeskakujeme hlavičku (začínáme od indexu 1 místo 0)
        for i in range(1, len(lines)):
            line = lines[i].strip()
            
            # Přeskočení prázdných řádků
            if not line:
                continue
            
            parts = line.split(';')
            
            # Bod 5.2 a 5.3 zadání: Ošetření proměnného počtu polí a validace dat
            # Očekáváme minimálně ČAS, CHECKPOINT a ID (3 pole)
            if len(parts) >= 3:
                try:
                    time_val = int(parts[0].strip())
                    ckpt = parts[1].strip()
                    id_cust = int(parts[2].strip())
                    
                    # Ošetření volitelné částky (např. u koncové pokladny)
                    cost_val = 0.0
                    if len(parts) > 3 and parts[3].strip():
                        cost_val = float(parts[3].strip())
                    
                    # Vytvoření instance Record a přidání do defaultdict pod správný checkpoint
                    city_data[ckpt].append(Record(
                        time=time_val, 
                        id_cust=id_cust,
                        cost=cost_val
                    ))
                except ValueError:
                    # Informujeme uživatele o přeskočení řádku se špatným typem (např. písmena místo čísel)
                    print(f"Přeskakuji nevalidní řádek {i+1} (špatný datový typ): {line}")
                    continue
            else:
                # Informujeme uživatele o přeskočení řádku, kde chybí základní sloupce
                print(f"Přeskakuji nevalidní řádek {i+1} (chybí sloupce): {line}")
                
    return city_data

def get_passed_set(data: dict[str, list[Record]], key_words: list[str]) -> set[int]:
    """Vrátí množinu (set) ID zákazníků, kteří prošli checkpointy začínajícími na key_words."""
    # Použití množiny (set) automaticky řeší duplicity. Pokud zákazník projde
    # více checkpointy (nebo stejným vícekrát), v množině bude figurovat pouze jednou.
    customers: set[int] = set()
    for ckpt, records in data.items():
        # Bod 3 zadání: Umožňuje vložit seznam prefixů a hledá shodu s kterýmkoliv z nich
        if any(ckpt.startswith(kw) for kw in key_words):
            for record in records:
                customers.add(record.id_cust)
    return customers

def filter_data_time(data: dict[str, list[Record]], cond_time: int) -> dict[str, list[Record]]:
    """Vrátí data obsahující pouze záznamy s časem <= cond_time."""
    ret: dict[str, list[Record]] = defaultdict(list)
    for ckpt, records in data.items():
        for record in records:
            if record.time <= cond_time:
                ret[ckpt].append(record)
            else:
                # Bod 6 zadání: Využití toho, že data jsou časově seřazená.
                # Jakmile narazíme na záznam s časem VĚTŠÍM než náš požadovaný (cond_time),
                # víme, že všechny další záznamy v tomto listu budou ještě novější.
                # Můžeme tedy cyklus pro tento checkpoint ukončit pomocí 'break'.
                # Tím ušetříme obrovské množství zbytečných průchodů!
                break
    return ret

def get_q_size(data: dict[str, list[Record]], seconds: int) -> int:
    """Spočítá velikost fronty před pokladnami v daný čas pomocí množinových operací."""
    # 1. Nejprve odřízneme záznamy, které se staly až v budoucnosti
    filtered_data = filter_data_time(data, seconds)
    
    # 2. Zjistíme, kdo se zařadil do fronty
    # Podle popisu zadání přicházejí zákazníci od zeleniny (vege), ovoce (fruit) nebo masa (meat).
    shoppers = get_passed_set(filtered_data, ["vege", "fruit", "meat"])
    
    # 3. Zjistíme, kdo už frontu opustil
    # Zákazníci opouštějí systém průchodem koncovou pokladnou (prefix "final").
    checkouts = get_passed_set(filtered_data, ["final"])
    
    # 4. Bod 1 a 4 zadání: Výpočet "zákazníci_přišli - zákazníci_odešli"
    # Protože shoppers i checkouts jsou datový typ 'set', můžeme použít rychlou 
    # operaci množinového rozdílu (znak mínus).
    in_queue = shoppers - checkouts
    
    return len(in_queue)

def histogram(data: dict[str, list[Record]]) -> None:
    """Vypíše stav fronty pro každou celou hodinu v datech (Bod 9 zadání)."""
    print(f"\n{'Hodina':<10} | {'Velikost fronty':<15}")
    print("-" * 30)
    
    # Celý den má 24 hodin (cyklus od 0 do 23)
    for h in range(24):
        # Převod hodin na sekundy (např. 15:00 je 15 * 3600 = 54000 sekund)
        time_sec = h * 3600
        size = get_q_size(data, time_sec)
        
        # Formátování výpisu na formát HH:00 (např. 08:00, 15:00)
        print(f"{f'{h:02d}:00':<10} | {size:<15}")

def main(data_path: str) -> None:
    # Nekonečná smyčka umožňující opakované dotazy od uživatele (Bod 10 zadání)
    while True:
        city = input("Zadejte město (Plzeň): ")
        shop = input("Zadejte obchod (shop_a): ")

        # Výchozí hodnoty pro usnadnění testování (pokud uživatel jen zmáčkne Enter)
        if city == "":
            city = "Plzeň"
        if shop == "":
            shop = "shop_a"

        data = load_data(data_path, city, shop)
        if data is None:
            # Pokud se data nepodařilo načíst (např. špatné jméno souboru), zeptáme se znovu
            continue

        histogram(data)

if __name__ == "__main__":
    # Ošetření argumentů příkazové řádky mimo samotný funkční kód (podmínka ze Zásad pro vypracování)
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_path>")
        sys.exit(1)
    
    # Spuštění hlavní logiky s předanou cestou ke kořenovému adresáři
    main(sys.argv[1])