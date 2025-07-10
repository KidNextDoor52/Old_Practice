import pandas as pd
import os

file_path = os.path.abspath("C:\\Users\\mccra\\OneDrive\\Documents\\GitHub\\Old_Practice\\day-25")
file = os.path.join(file_path, "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data = pd.read_csv(file)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


squirrel_dict = {
"Fur Color": ["Gray", "Cinnamon", "Black"],
"Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pd.DataFrame(squirrel_dict)
df.to_csv("day-25/squirrel_count.csv")
