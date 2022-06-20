def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    elements = [3, 9, 4, 16, 11, 78, 67, 1]
    selection_sort(elements)
    print(elements)