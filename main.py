from collections import deque

def BFS(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    pass

def DFS(graph, vertex, visited):
    visited.add(vertex)
    print(vertex,end=' ')

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            DFS(graph,neighbour,visited)

def main():
    graph = {
        0: [1, 2, 4],
        1: [0, 2, 3, 5],
        2: [0, 1, 6],
        3: [1, 5, 7],
        4: [0, 6, 7],
        5: [1, 3, 7],
        6: [2, 4],
        7: [3, 4, 5]
    }

    visited = set()
    start_vertex = 0
    # DFS(graph, start_vertex, visited)
    BFS(graph, start_vertex)

if __name__ == '__main__':
    main()



