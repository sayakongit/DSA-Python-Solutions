array = []
with open("nyc_weather.csv", "r") as f:
    for i in f:
        temp = i.split(",")
        deg = temp[1][:-1]
        array.append(deg)

array = list(map(int, array[1:]))

t = 0
m = array[0]

for i, v in enumerate(array):
    if i < 7:
        t += v
    if v > m:
        m = v

avg = t / 7
print("The average temperature of 1st 7 days is", round(avg, 2))
print("The maximum temperature of 10 days is", m)