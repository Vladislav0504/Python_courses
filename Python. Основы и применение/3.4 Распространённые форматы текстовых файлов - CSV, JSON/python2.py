"""JSON format."""
from json import loads

from collections import deque


def search(parent: str, edges: dict[str, list[str]],
           children: dict[str, set[str]]) -> None:
    """Breadth-first search - BFS."""
    queue = deque([parent])
    children[parent].add(parent)
    while queue:
        vertex = queue.popleft()
        for elem in edges[vertex]:
            if elem not in children[parent]:
                queue.append(elem)
                children[parent].add(elem)


def main():
    """My function."""
    data, edges, children = loads(input()), {}, {}
    for elem in data:
        children[elem["name"]] = set()
        edges.setdefault(elem["name"], [])
        for parent in elem["parents"]:
            edges.setdefault(parent, []).append(elem["name"])
    for par in children:
        search(par, edges, children)
    for key, value in children.items():
        children[key] = len(value)
    print(*(f"{name} : {k}" for name, k in sorted(children.items())), sep="\n")


if __name__ == "__main__":
    main()
