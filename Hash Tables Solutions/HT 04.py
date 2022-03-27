arr = []
with open("poem.txt", "r") as p:
    for i in p:
        temp = i.split(" ")
        arr.append(temp)

print(arr)

