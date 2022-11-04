def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid_index = len(arr) // 2
    left, right = arr[:mid_index], arr[mid_index:]
    left = merge_sort(left)
    right = merge_sort(right)

    def merge_two_arrays(array1, array2):
        ret_list = []
        i, j = 0, 0
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                ret_list.append(array1[i])
                i += 1
            else:
                ret_list.append(array2[j])
                j += 1
        return ret_list + array1[i:] + array2[j:]

    return merge_two_arrays(left, right)


merge_sort([1, 5, 3, 9, 0, 2, 3, 2])
