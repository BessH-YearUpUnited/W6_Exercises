import csv

def parse_csv(filepath):

    data = []

    with open(filepath, "r") as f:
        csv_reader = csv.reader(f)

        for i in csv_reader:
            data.append(i)
    
    return data

survey_data = parse_csv("survey_data.csv")

print(survey_data[:5])
print(type(survey_data))
