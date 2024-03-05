def triplet(arr, p):
    for i in range(0, len(arr) - 1):
        temp = p - arr[i]
        for j in range(i + 1, len(arr)):
            if (temp - arr[j]) in arr[j+1:]:
                return True
    return False


arr1 = [1, 1, 1, 10, 10, 10]
print(triplet(arr1, 3))
