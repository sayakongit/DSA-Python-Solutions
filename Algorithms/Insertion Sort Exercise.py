def calculateMedian(nums):
    size = len(nums)
    if size % 2 != 0:
        median = nums[size // 2]
    else:
        median = (nums[size // 2] + nums[size // 2 - 1]) / 2

    if median == int(median):
        median = int(median)
    return median


def insertion_sort(arr):
    for i in range(len(arr)):
        anchor = arr[i]
        j = i - 1
        med_arr = arr[:j+1]
        if med_arr:
            print(calculateMedian(med_arr))
        while j >= 0 and arr[j] > anchor:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor
        if i == len(arr)-1:
            print(calculateMedian(arr))


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
