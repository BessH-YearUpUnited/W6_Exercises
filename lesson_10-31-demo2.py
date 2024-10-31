# Open the file # Read the file # Close the file

with open("survey_data.csv", "r") as f:
    data = f.readlines()

data_list = []

for i in data:
    data_list.append(i.split(','))

# print(data_list[0][2])
# print(data_list[1][2])

ages = []

for i in data_list:
    ages.append(i[2])

ages.pop(0)

# print(f'List of ages: {ages}')

ages_file = open("survey_ages.txt", "a")
ages_file.write("List of ages from survey_data.csv")
ages_file.close()