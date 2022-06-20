def insertion_sort(elements):
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > anchor:
            # elements[j], elements[j+1] = elements[j+1], elements[j]
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor


if __name__ == '__main__':
    arr = [3, 9, 4, 16, 11, 78, 67, 1]
    insertion_sort(arr)
    print(arr)