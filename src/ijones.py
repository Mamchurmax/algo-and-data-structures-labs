def read_input(file_path):
    file = open(file_path, 'r')
    try:
        columns, lines = map(int, file.readline().split(' '))
    except ValueError:
        file.close()
        return 0

    matrix = []
    dict_of_letters = dict()
    cur_line = 0
    for line in file:
        line = line.replace('\n', '')
        cur_column = 0
        temp_line = []
        for char in line:
            temp_line.append(char)
            if char in dict_of_letters:
                dict_of_letters[char].append((cur_line, cur_column))
            else:
                dict_of_letters[char] = [(cur_line, cur_column)]

            cur_column += 1

        matrix.append(temp_line)
        cur_line += 1
    file.close()
    return matrix, dict_of_letters, lines, columns


def get_result(matrix, dict_of_letters, rows, columns):
    total_paths = 0
    for j in range(rows):
        queue = [(j, 0)]
        while queue:
            cur_row, cur_col = queue.pop(0)
            if cur_col == columns - 1:
                if cur_row == 0 or cur_row == rows - 1:
                    total_paths += 1
                continue

            for same_letter in dict_of_letters[matrix[cur_row][cur_col]]:
                if same_letter[1] > cur_col:
                    queue.append(same_letter)

            if (cur_row, cur_col + 1) not in queue:
                queue.append((cur_row, cur_col + 1))

    return total_paths


def write_output(output_file, result):
    with open(output_file, 'w') as file:
        file.write(str(result))


def indiana_jones(input_file, output_file):
    input_data = read_input(input_file)
    if input_data == 0:
        write_output(output_file, 0)
        return

    indiana_jones_matrix, letters_dict, rows, columns = input_data
    result = get_result(indiana_jones_matrix, letters_dict, rows, columns)
    write_output(output_file, result)

