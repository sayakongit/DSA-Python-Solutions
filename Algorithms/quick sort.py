def swap(a, b, elements):
    if a != b:
        elements[a], elements[b] = elements[b], elements[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        p = partition(elements, start, end)
        quick_sort(elements, start, p-1)
        quick_sort(elements, p+1, end)


if __name__ == '__main__':
    elements = [7, 2, 45, 4, 14, 78, 62]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)