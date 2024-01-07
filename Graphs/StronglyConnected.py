'''Check if the graph is strongly connected'''


def create_graph(adj_matrix, graph):
    for index in range(len(adj_matrix)):
        graph[index] = []
        for edge_index in range(len(adj_matrix[index])):
            if adj_matrix[index][edge_index] == 1:
                graph[index].append(edge_index)


def dfs(graph, starting_vertex, visited):
    visited[starting_vertex] = 1
    for adjacent in graph[starting_vertex]:
        if visited[adjacent] == 0:
            dfs(graph, adjacent, visited)


def Is_Connected(n, graph):
    for i in range(n):
        visited = [0] * n
        dfs(graph, i, visited)
        for j in visited:
            if j == 0:
                return False
    return True


if __name__ == "__main__":
    n = 4;
    graph = {}
    adj_matrix = [[1, 1, 0, 0]
        , [1, 0, 0, 1]
        , [0, 0, 0, 1]
        , [1, 0, 1, 0]]
    create_graph(adj_matrix, graph)
    # Function call
    if (Is_Connected(n, graph)):
        print("Yes");
    else:
        print("No");