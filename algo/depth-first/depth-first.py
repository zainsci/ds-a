#! /bin/python3

def depth_first(graph, source):
    stack = [source]
    path = []

    while len(stack) > 0:
        curr = stack.pop()
        if curr not in path:
            path.append(curr)

        for i in graph[curr]:
            if i not in path:
                stack.append(i)
    return path


def main():
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": [],
        "e": ["b"],
        "f": ["d"],
    }
    path = depth_first(graph, "a")
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
    path = depth_first(graph, "a")
    print(path)


if __name__ == "__main__":
    main()
