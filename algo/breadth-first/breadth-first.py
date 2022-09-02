#! /bin/python3

def breadth_first(graph, source):
    queue = [source]
    path = []

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr not in path:
            path.append(curr)

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


if __name__ == "__main__":
    main()
