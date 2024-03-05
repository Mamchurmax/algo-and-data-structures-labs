def triplet(arr, p):
    arr = sorted(arr)
    for i in range(len(arr) - 2):
        temp = p - arr[i]
        left = i + 1
        right = len(arr) - 1
        while left < right:
            sum_of2 = arr[left] + arr[right]
            if sum_of2 == temp:
                return True
            elif sum_of2 < temp:
                left += 1
            else:
                right -= 1
    return False
