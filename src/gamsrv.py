from src.heap_based_priority_queue import *


def dijkstra(server, vertex_n, clients, adjacency_list):
    temp_max_ping = 0
    priority_queue = PriorityQueue()
    priority_queue.insert(server, 0)
    dist_to = {}
    for vertex in range(vertex_n + 1):
        dist_to[vertex] = float('inf')
    dist_to[server] = 0
    visited = set()
    while priority_queue:
        node = priority_queue.delete_root()
        if node is None:
            break
        vertex = node[0]
        if vertex in clients:
            temp_max_ping = max(temp_max_ping, dist_to[vertex])
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbour, weight in adjacency_list[vertex - 1]:
            if dist_to.get(neighbour, float('inf')) > dist_to[vertex] + weight:
                dist_to[neighbour] = dist_to[vertex] + weight
                priority_queue.insert(neighbour, dist_to[neighbour])
    return temp_max_ping


def ping(input_file, output_file):
    file = open(input_file, 'r')
    try:
        vertex_n, edge_n = tuple(map(int, file.readline().split(' ')))
        gamers = list(map(int, file.readline().split(' ')))
        router_list = [router for router in range(1, vertex_n + 1) if router not in gamers]
        adjacency_list = [[] for _ in range(vertex_n)]
        for _ in (range(edge_n)):
            vertex, neighbour, weight = tuple(map(int, file.readline().split(' ')))
            adjacency_list[vertex - 1].append((neighbour, weight))
            adjacency_list[neighbour - 1].append((vertex, weight))
        file.close()
    except ValueError:
        write_output(output_file, None)
        file.close()
        return

    min_max_ping = float('inf')
    max_server = None
    for server in router_list:
        current_ping = dijkstra(server, vertex_n, gamers, adjacency_list)
        if current_ping < min_max_ping:
            min_max_ping = current_ping
            max_server = server

    with open(output_file, 'w') as file:
        file.write(str(min_max_ping))
        file.write(str(max_server))
    return


def write_output(output_file_path, result):
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()
    return


input_file = 'C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_1.in.txt'
output_file = 'C:/Projects/algo-and-data-structures-labs/resources/lab6/test_output.txt'
ping(input_file, output_file)
