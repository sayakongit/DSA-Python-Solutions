def bubble_sort(arr):
    size = len(arr)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    arr = [3, 9, 4, 16, 11, 78, 67, 1]
    bubble_sort(arr)
    print(arr)
