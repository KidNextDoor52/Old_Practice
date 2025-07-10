import os

#script_dir = os.path.abspath("C:\\Users\\mccra\\OneDrive\\Documents\\GitHub\\Old_Practice\\day 25")
#file_to_open = os.path.join(script_dir, "weather_data.csv")
#
#
#with open(file_to_open) as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv
#
#script_dir = os.path.abspath("C:\\Users\\mccra\\OneDrive\\Documents\\GitHub\\Old_Practice\\day 25")
#file = os.path.join(script_dir, "weather_data.csv")
#
#with open (file) as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)
import pandas as pd


script_dir = os.path.abspath("C:\\Users\\mccra\\OneDrive\\Documents\\GitHub\\Old_Practice\\day-25")
file = os.path.join(script_dir, "weather_data.csv")

#data = pd.read_csv(file)
#
##data_dict = data.to_dict()
##print(data_dict)
##
##temp_list = data["temp"].to_list()
##print(temp_list)
##
##print(len(temp_list))
##
##print(data["temp"].max())
##
###get data in columns
##print(data["condition"])
##print(data.condition)
#
##get data in row
##print(data[data.day == "Monday"]) 
##print(data[data.temp == data.temp.max()])
#
#monday = data[data.day == "Monday"]
#print(monday.condition)
#
#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)

#CREATE DATAFRAM FROM SCRATCH

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 54, 34]

}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv("day-25/new_data.csv")