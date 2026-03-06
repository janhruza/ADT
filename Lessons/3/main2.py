# Řešení získané z Discordu předmětu ADT
# Autor originálního příspěvku s kódem: Rastislav Lipták

from collections import defaultdict
import os
import sys
from dataclasses import dataclass

@dataclass
class Record:
    time: int
    id_cust: int

def load_data(data_path: str, city: str, shop: str, day: str = "1-Mon") -> dict[str, list[Record]] | None:
    """ Funkce načte data z daného souboru a vrátí je jako slovník.
    Klíčem je název checkpointu a hodnotou je list záznamů.

    Args:
        data_path (str): cesta k adresáři se všemi daty
        city (str): název města, které chceme načíst
        shop (str): název obchodu, který chceme načíst
        day (str, optional): Konkrétní den, který chceme načíst. Defaults to "1-Mon".

    Returns:
        dict[str, list[Record]] | None: slovník s načtenými daty nebo None pokud soubor neexistuje
    """

    # pozn. Můžeme použít default dict, nebo použít běžný slovník a při přidání nového záznamu
    # vždy zkontrolovat, zda klíč již existuje, případně inicializovat prázdný list

    city_data: dict[str, list[Record]] = {}
    # city_data: dict[str, list[Record]] = defaultdict(list)

    file_path = os.path.join(data_path, city, day, f"{shop}.txt")
    with open(file_path) as file:
        for line in file:
            data = line.strip()
            div_data = data.split(";")
            if len(div_data) != 4:
                continue

            try:
                time = int(div_data[0])
                ckpt = div_data[1]
                cus_id = int(div_data[2])
            except Exception:
                continue

            record = Record(time, cus_id)

            if ckpt not in city_data:
                city_data[ckpt] = []
            city_data[ckpt].append(record)


    print("loading", city)

    return city_data

def get_passed_set(data: dict[str, list[Record]], key_words: list[str]) -> set[int]:
    """Funkce vrátí množinu zákazníků, kteří prošli alespoň jedním z checkpointů s prefixem
    předaných jako key_words. Do funkce tedy nevstupuje celé jméno checkpointu ale pouze
    jeho prefix (např. vege místo vege_1).

    Args:
        data (dict[str, list[Record]]): data načtená z datového souboru funkcí load_data
        key_words (list[str]): prefixové označení checkpointů, které chceme sledovat

    Returns:
        set[int]: Funkce vrací množinu identifikačních čísel zákazníků.
    """
    customers: set[int] = set()
    for ckpt, rcs in data.items():
        # found = False
        for k in key_words:
            if ckpt.startswith(k):
                for record in rcs:
                    customers.add(record.id_cust)
    return customers

def filter_data_time(data: dict[str, list[Record]], cond_time: int) -> dict[str, list[Record]]:
    """Funkce vrátí data omezená na záznamy s časem menším nebo rovným než je cond_time.
    Args:
        data (dict[str, list[Record]]): data načtená z datového souboru funkcí load_data
        cond_time (int): časový limit v sekundách
    Returns:
        dict[str, list[Record]]: vrací data omezená na záznamy s časem menším nebo rovným cond_time.
    """
    ret: dict[str, list[Record]] = defaultdict(list)
    for key, value in data.items():
        for rec in value:
            if rec.time <= cond_time:
                ret[key].append(rec)
    return ret

def get_q_size(data: dict[str, list[Record]], seconds: int) -> int:
    """Funkce vrátí velikost fronty v daném čase.
    Velikost fronty je dána počtem zákazníků, kteří prošli některým z checkpointů
    (vege, frui, meat) a ještě neprošli pokladnou.
    """
    filtered_data = filter_data_time(data, seconds)
    was_at_final_ckpt = get_passed_set(filtered_data, ["final-crs"])
    was_at_mid_ckpt = get_passed_set(filtered_data, ["vege", "frui", "meat"])

    result = len(was_at_mid_ckpt) - len(was_at_final_ckpt)
    result = len(was_at_mid_ckpt.difference(was_at_final_ckpt))
    return result

def histogram(data: dict[str, list[Record]]) -> None:
    for hour in range(24):
        sec = hour * 60 * 60

        result = get_q_size(data, sec)
        print(f"{hour} - {result}")

def main(data_path: str) -> None:
    while True:
        city = input("Zadejte město (Plzeň): ")
        shop = input("Zadejte obchod (shop_a): ")

        if city == "":
            city = "Plzeň"
        if shop == "":
            shop = "shop_a"

        data = load_data(data_path, city, shop)
        if data is None:
            continue

        histogram(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_path>")
        sys.exit(1)
    main(sys.argv[1])