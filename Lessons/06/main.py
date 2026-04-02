# Vyplneny ukol z 6. cviceni KIV/ADT
# Autor reseni: Jan Hruza
# Datum: 2026-03-27

import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))



def worker_tick(worker: Worker) -> None:
    if worker.timer > 0:
        worker.timer -= 1
    else:
        if worker.source:
            item = worker.source.popleft()
            worker.dest.append(item)
            worker.timer = get_delay(worker.period, worker.spread_factor)


def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Time: {time}s")
    for name, queue in queues:
        print(f"  {name}: {len(queue)} people")
    print("-" * 30)


def main() -> None:
    people_number = 1000
    people_in_the_city = deque(list(range(people_number)))

    # 1. Vytvoření front
    day_queue = deque(list(range(people_number)))
    gate_queue = deque()
    vege_queue = deque()
    final_queue = deque()
    done_queue = deque()

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe = [
        ("Day", day_queue),
        ("Gate", gate_queue),
        ("Vege", vege_queue),
        ("Cashier", final_queue),
        ("Done", done_queue)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30          # Každých 30s přijde někdo z ulice
    gate_m = 5          # Gate keeper každého odbavuje 5s
    vege_m = 45         # Vážení zeleniny trvá 45s
    final_m = 2 * 60    # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    day_worker = Worker("Generator", day_queue, gate_queue, day_m)
    gate_worker = Worker("Gate Keeper", gate_queue, vege_queue, gate_m)
    vege_worker = Worker("VegeMan", vege_queue, final_queue, vege_m, spread_factor=0.2)
    final_worker = Worker("Cashier", final_queue, done_queue, final_m, spread_factor=0.1)

    # 3. Hlavní smyčka simulace
    simulation_time = 2 * 60 * 60  # Simulace na 2 hodiny (v sekundách)
    for current_time in range(simulation_time):
        worker_tick(day_worker)
        worker_tick(gate_worker)
        worker_tick(vege_worker)
        worker_tick(final_worker)

        # Výpis stavu každou hodinu
        if current_time % 60 == 0:
            print_snapshot(current_time, queues_to_observe)

if __name__ == "__main__":
    main()
