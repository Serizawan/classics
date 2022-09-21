def bfs(graph, start_node):
    queue = [start_node]
    visited = set(start_node)
    bfs_ordering = [start_node]
    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
                bfs_ordering.append(n)
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
