# 01_hledani_podmatice_s_maximalnim_souctem.py
# autor reseni: Jan Hruza
# datum: 2026-04-02

import numpy as np

def search_max_sum(field: np.ndarray, size: int) -> tuple[int, np.ndarray] | None:
    """
    Najde čtverec dané velikosti s maximálním součtem prvků.

    Args:
        field (np.ndarray): Vstupní 2D pole čísel.
        size (int): Velikost strany hledaného čtverce.

    Returns:
        tuple[int, np.ndarray] | None: N-tice obsahující maximální součet a
        odpovídající čtverec. Pokud se čtverec dané velikosti do pole nevejde,
        vrátí None.
    """
    # TODO Zkontrolujte, zda se čtverec dané velikosti do pole vejde. Pokud ne, vraťte None.
    # Poté projděte všechny možné pozice čtverce a nalezněte tu s maximálním součtem prvků.
    # Vraťte maximální součet a odpovídající výřez pole.
    if size > field.shape[0] or size > field.shape[1]:
        # čtverec se nevejde do pole
        return None
    
    max_sum = None
    max_square = None

    # projdeme všechny možné pozice pro levý horní roh čtverce o velikosti size x size
    for i in range(field.shape[0] - size + 1):

        # projdeme všechny možné pozice čtverce o velikosti size x size
        for j in range(field.shape[1] - size + 1):
            square = field[i:i+size, j:j+size]
            current_sum = np.sum(square)

            # ověříme, zda je tento součet větší než dosud nalezený maximální součet
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
                max_square = square

    return max_sum, max_square

def main():
    """
    Hlavní funkce pro demonstraci hledání čtverce s maximálním součtem.
    """
    rows = 10
    cols = 15
    field_sequential = np.arange(rows * cols, dtype=int).reshape(rows, cols)
    print("Testovací pole 1 (sekvenční):")
    print(field_sequential)

    size = 3
    result = search_max_sum(field_sequential, size)
    if result:
        max_sum, square = result
        print(f"\nNejvětší součet prvků ve čtverci {size}x{size} je: {max_sum}")
        print("Čtverec:")
        print(square)
    else:
        print(f"\nDo pole se nevejde čtverec o velikosti {size}x{size}.")

    print("-" * 30)

    rows = 20
    cols = 5
    # Vytvoříme náhodné pole s hodnotami mezi 0 a 99 a rozměry 20x5
    field_random = np.random.randint(100, size=(rows, cols), dtype=int)
    print("\nTestovací pole 2 (náhodné):")
    print(field_random)
    
    result_random = search_max_sum(field_random, size)
    if result_random:
        max_sum_random, square_random = result_random
        print(f"\nNejvětší součet prvků ve čtverci {size}x{size} je: {max_sum_random}")
        print("Čtverec:")
        print(square_random)
    else:
        print(f"\nDo pole se nevejde čtverec o velikosti {size}x{size}.")

main()
