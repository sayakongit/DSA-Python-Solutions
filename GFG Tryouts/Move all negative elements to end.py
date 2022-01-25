# arr = [1, -1, 3, 2, -7, -5, 11, 6]
arr = [-5, 7, -3, -4, 9, 10, -1, 11]
p = []
n = []

for i in range(len(arr)):
    if arr[i] < 0:
        n.append(arr[i])
    else:
        p.append(arr[i])

print(p+n)