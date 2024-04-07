def labyrinth(start_point, goal, size, lab):
    q = [start_point]
    distance = {start_point: 0}
    visited = set()
    while q:
        vertex = q.pop(0)
        if vertex in visited:
            continue
        if vertex == goal:
            return distance[vertex]
        visited.add(vertex)
        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x, y = vertex[1] + direction[1], vertex[0] + direction[0]
            if (0 <= y < size[0] and 0 <= x < size[1] and (x, y) not in visited and
                    lab[x][y] != 0):
                q.append((x, y))
                distance[(x, y)] = distance[vertex] + 1
    return None


def read_input(input_file):
    with open(input_file, 'r') as f:
        start = tuple(map(int, f.readline().strip().split(', ')))
        goal = tuple(map(int, f.readline().strip().split(', ')))
        size = tuple(map(int, f.readline().strip().split(', ')))
        lab = []
        for _ in range(size[0]):
            row_str = f.readline().strip()
            row = [int(x) for x in row_str[1:-1].split(', ')]
            lab.append(row)
    return start, goal, size, lab


def write_output(output_file, result):
    with open(output_file, 'w') as f:
        f.write(str(result))


def main():
    input_file = 'C:/Projects/algo-and-data-structures-labs/resources/input.txt'
    output_file = 'C:/Projects/algo-and-data-structures-labs/resources/output.txt'
    start, goal, size, lab = read_input(input_file)
    result = labyrinth(start, goal, size, lab)
    write_output(output_file, result)


if __name__ == '__main__':
    main()
