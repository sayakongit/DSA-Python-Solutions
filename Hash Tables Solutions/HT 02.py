data = {}
with open("nyc_weather.csv", "r") as f:
    for i in f:
        temp = i.split(",")
        data[temp[0]] = temp[1][:-1]

print(f"Temperature on Jan 9 was {data['Jan 9']} degree ")
print(f"Temperature on Jan 4 was {data['Jan 4']} degree ")