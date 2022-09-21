def bfs(graph, start_node):
    bfs_ordering = []
    visited = set(start_node)
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        bfs_ordering.append(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
    return bfs_ordering


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["D"],
        "D": ["E", "A"],
        "E": [],
    }
    assert(bfs(graph, "A") == ["A", "B", "C", "D", "E"])
