def read_input(input_file,):
    adj_matrix = []
    with open(input_file, 'r') as f:
        for line in f:
            row = list(map(int, line.split(',')))
            adj_matrix.append(row)
    return adj_matrix


def prim(matrix):
    num_vertices = len(matrix)
    if num_vertices == 0:
        return -1
    visited = [False] * num_vertices
    start_vertex = 0
    visited[start_vertex] = True
    mst_len = 0
    edges = []

    for neighbor in range(num_vertices):
        if matrix[start_vertex][neighbor] != 0:
            edges.append((matrix[start_vertex][neighbor], start_vertex, neighbor))

    while not all(visited):
        min_edge = None
        for edge in edges:
            weight, cur_vertex, next_vertex = edge
            if (visited[cur_vertex] and not visited[next_vertex]) or (visited[next_vertex] and not visited[cur_vertex]):
                if min_edge is None or weight < min_edge[0]:
                    min_edge = edge

        if min_edge:
            weight, cur_vertex, next_vertex = min_edge
            visited[next_vertex] = True
            mst_len += weight

            for neighbor in range(num_vertices):
                if matrix[next_vertex][neighbor] != 0 and not visited[neighbor]:
                    edges.append((matrix[next_vertex][neighbor], next_vertex, neighbor))

    return mst_len
