# 00_strom_a_graf.py
# autor reseni: Jan Hruza
# datum: 2026-04-27

# Komentare k reseni byly vygenerovany umelou inteligenci a mohou obsahovat chyby.
# Pokud neco nebude fungovat, zkuste se zamyslet nad tim, co se deje a proc.

from collections import deque

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
    Finds and returns one path from start_node_val to target_val using BFS.
    Returns a tuple of:
      - a list of node values representing the path if found, otherwise None
      - a list of node values in the order they were discovered during BFS
    """
    
    # TODO Implementujte BFS algoritmus pro nalezení nejkratší cesty ze startu do cíle.
    # Použijte frontu pro uzly k navštívení, množinu pro sledování navštívených uzlů,
    # a slovník pro uložení rodičovských odkazů pro rekonstrukci cesty.
    queue = deque([start_node_val])
    parents: dict[int, int | None] = {start_node_val: None}
    visited = {start_node_val}
    discovery_order: list[int] = [start_node_val]

    # Dokud fronta není prázdná, pokračujte v prohledávání
    while queue:
        current_node = queue.popleft()

        # Pokud jsme našli cílový uzel, rekonstruujeme cestu a vrátíme ji spolu s pořadím objevování
        if current_node == target_val:
            path = []

            # Rekonstruujeme cestu zpět pomocí rodičovských odkazů
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]

            # Cestu vracíme v správném pořadí (od startu k cíli) a pořadí objevování
            return path[::-1], discovery_order

        # Pro každý sousední uzel, který ještě nebyl navštíven, ho přidáme do fronty a označíme jako navštívený
        for weight, neighbor in graph.edges.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node
                queue.append(neighbor)
                discovery_order.append(neighbor)

    # Pokud jsme prošli všechny uzly a nenalezli cílový uzel, vracíme None a pořadí objevování
    return None, discovery_order

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

