f = open("survey_data.csv")

data = f.readlines()

f.close()

# print(data[0:4])
# print(type(data))

lines = []
for i in data:
    lines.append(i.split(','))

print(lines[:4])

ages = []

for i in lines:
    ages.append(i[2])

# print(ages)