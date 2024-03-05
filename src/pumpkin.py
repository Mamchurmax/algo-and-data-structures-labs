def pumpkin(array):
    start_list = []
    columns = len(array[0])
    lenght = len(array)
    final_list = []
    for i in range(columns):
        for j in range(lenght):
            start_list.append(array[j][i])
        if i % 2 == 0:
            start_list.reverse()
        final_list.extend(start_list)
        start_list = []
    return final_list


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(pumpkin(arr))
