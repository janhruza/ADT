# 01_strom_a_graf_dfs.py
# autor reseni: Jan Hruza
# datum: 2026-04-27

# Komentare k reseni byly vygenerovany umelou inteligenci a mohou obsahovat chyby.
# Pokud neco nebude fungovat, zkuste se zamyslet nad tim, co se deje a proc.

class Graph:
    """
    A simple undirected graph representation.
    """
    def __init__(self) -> None:
        self.edges: dict[int, list[tuple[float, int]]] = {}

    def add_edge(self, src: int, dst: int, weight: float = 0) -> None:
        """
        Adds an undirected edge between src and dst.
        """
        if src not in self.edges:
            self.edges[src] = []
        if dst not in self.edges:
            self.edges[dst] = []

        self.edges[src].append((weight, dst))
        self.edges[dst].append((weight, src))


def find_path(graph: Graph, start_node_val: int, target_val: int) -> tuple[list[int] | None, list[int]]:
    """
    Finds and returns one path from start_node_val to target_val using DFS.
    Returns a tuple of:
      - a list of node values representing the path if found, otherwise None
      - a list of node values in the order they were discovered during DFS
    """

    # TODO Implementujte DFS algoritmus pro nalezení cesty ze startu do cíle.
    # Použijte zásobník pro uzly k navštívení, množinu pro sledování navštívených uzlů,
    # a slovník pro uložení rodičovských odkazů pro rekonstrukci cesty.

    stack = [start_node_val]
    visited = set()
    parent = {start_node_val: None}
    discovered = []

    # Provedeme DFS průchod grafem
    while stack:
        current = stack.pop()

        # Pokud jsme tento uzel ještě nenavštívili, zpracujeme ho
        if current not in visited:
            visited.add(current)
            discovered.append(current)

            # Pokud jsme dosáhli cíle, můžeme ukončit hledání
            if current == target_val:
                break

            # Získáme sousedy (pouze hodnoty uzlů)
            neighbors = [n for _, n in graph.edges.get(current, [])]
            
            # Pro DFS přidáváme sousedy na zásobník v opačném pořadí, aby se prohledávali v původním pořadí
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    # Uložíme rodiče pouze pokud uzel ještě neznáme
                    if neighbor not in parent:
                        parent[neighbor] = current
                    stack.append(neighbor)

    # Pokud jsme nenašli cílový uzel, vrátíme None a pořadí objevování
    if target_val not in visited:
        return None, discovered

    # Rekonstruujeme cestu z cíle zpět k startu pomocí rodičovských odkazů
    path = []
    curr = target_val
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    
    # Cesta je sestavena v opačném pořadí, takže ji obrátíme
    return path[::-1], discovered


if __name__ == '__main__':
    tree = Graph()
    tree.add_edge(1, 2)
    tree.add_edge(1, 3)
    tree.add_edge(1, 4)
    tree.add_edge(2,5)
    tree.add_edge(2,6)
    tree.add_edge(3,7)

    print("\nSearching for node 7 in the tree starting from 1...")
    path, discovered = find_path(tree, 1, 7)
    print("Discovery order:", discovered)
    if path:
        path_str = [str(node) for node in path]
        print("Found path:", " -> ".join(path_str))
