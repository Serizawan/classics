def dfs(graph, start_node, visited, dfs_ordering):
    if start_node not in visited:
        visited.add(start_node)
        dfs_ordering.append(start_node)
        for n in graph[start_node]:
            dfs(graph, n, visited, dfs_ordering)
    return dfs_ordering


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["D"],
        "D": ["E", "A"],
        "E": [],
    }
    assert(dfs(graph, "A", set(), []) == ["A", "B", "D", "E", "C"])
