import functools

from utils import measure_time

def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

@functools.cache
def fib_cache(n: int) -> int:
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

def fib_mem(n: int, lookup: dict[int, int]) -> int:
    if n <= 1:
        return n

    if n not in lookup:
        lookup[n] = fib_mem(n - 1,lookup) + fib_mem(n - 2,lookup)

    return lookup[n]


def fib_table(n: int) -> int:
    """
    Vytvoříme tabulku, do které postupně doplníme všechny Fibonacciho čísla až do n-tého.
    Bottom-up přístup, protože začínáme od nejmenších hodnot a postupujeme směrem k n-tému.
    """

    # Vytvoříme tabulku, která bude mít n+1 prvků (pro indexy 0 až n).
    table: list[int] = [0, 1] + [0] * (n - 1)

    # Postupně doplňujeme tabulku od indexu 2 až do n-tého indexu.
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

def fib_const(n: int) -> int:
    """
    Výpočet Fibonacciho čísla pomocí konstantího prostoru. Jako list, ale uchováváme jen dvě poslední hodnoty.
    """
    
    if n <= 1:
        return n

    # Inicializace dvou posledních hodnot
    prev2, prev1 = 0, 1

    # Postupný výpočet Fibonacciho čísla
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1

def main() -> None:
    LIMIT = 100
    lookup: dict[int, int] = {}

    a = 20 # to je hned
    # a = 30 # to už chvilku trvá
    # a = 40 # za jak dlouho se asi dočkáme?

    measure_time(lambda: fib_cache(a), LIMIT)
    measure_time(lambda: fib_mem(a, lookup), LIMIT)
    measure_time(lambda: fib(a), LIMIT)
    measure_time(lambda: fib_table(a), LIMIT)
    measure_time(lambda: fib_const(a), LIMIT)

if __name__ == "__main__":
    main()
