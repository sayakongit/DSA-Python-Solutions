trains = { 12121: [15, 20],
           12311: [5, 15],
           17215: [2, 5]}

f = 12311

p1 = [[]]*len(trains)

sort_trains = sorted(trains.items(), key=lambda x: x[1])

p1[0].append(sort_trains[0][0])
j = 0

for i in sort_trains[1:]:
    if i[1][0] > trains[p1[0][-1]][1]:
        j = 0
        p1[j].append(i[0])
    else:
        j += 1
        p1[j].append(i[0])


print(p1)
