#! /bin/python3

def gen_graph(edges):
    graph = {}

    for edge in edges:
        if edge[0] not in graph.keys():
            graph[edge[0]] = [edge[1]]
        else:
            graph[edge[0]].append(edge[1])

        if edge[1] not in graph.keys():
            graph[edge[1]] = [edge[0]]
        else:
            graph[edge[1]].append(edge[0])

    return graph


def breadth_first(graph, source):
    queue = [source]
    path = set()

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr not in path:
            path.add(curr)

        for i in graph[curr]:
            if i not in path:
                queue.append(i)

    return path


def main():
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": [],
    }
    path = breadth_first(graph, "a")
    print(path)

    graph = {
        "a": ["h", "g"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f", "g"],
        "e": ["a"],
        "f": ["b", "a"],
        "g": ["c", "e", "h"],
        "h": ["g", "a", "b"]
    }
    path = breadth_first(graph, "a")
    print(path)

    edges = [
        ["i", "j"],
        ["k", "i"],
        ["k", "j"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"],
    ]
    graph = gen_graph(edges)
    path = breadth_first(graph, "i")
    print(path)


if __name__ == "__main__":
    main()
