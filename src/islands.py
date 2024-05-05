from typing import List

def read_input(input_file: str):
    """
    Read the input file and return the adjacency matrix
    :param input_file: the path to the input file
    :return: the adjacency matrix of the graph
    """
    adj_matrix = []
    with open(input_file, 'r') as f:
        for line in f:
            row = list(map(int, line.split(',')))
            adj_matrix.append(row)
    return adj_matrix


def floyd_warshall(matrix: List[List[int]]) -> List[List[int]]:
    """
    :param adjacency matrix:
    :return matrix of shortest paths between all pairs of vertices:
    """
    n = len(matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix


def min_cable_length(matrix: list[list[int]]) -> int:
    """
    :param matrix of shortest paths between all pairs of vertices matrix:
    :return length of all cables needed to connect all islands:
    """
    matrix1 = floyd_warshall(matrix)
    n = len(matrix1)
    total_length = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                total_length += matrix1[i][j]
    return total_length
