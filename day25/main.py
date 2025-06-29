
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# Two types of data structures(data types) in pandas: series and DataFrames
# print(type(data))
# print(type(data["temp"]))

# Conversion of csv file(dataframe) into dictionary
data_dict = data.to_dict()
# print(data_dict)

# Conversion of series to List
temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# calculating average of temperature
# avg = sum(temp_list)/ (len(temp_list))
# print(avg)
#OR
# print(data["temp"].mean())

# get max value
# print(data["temp"].max())

#get data in columns
# print(data["condition"])
#OR
# print(data.condition)


# Get data in Rows
# print(data[data.day == "Monday"])


#print the row of data which had the highest temperature
# print(data[data.temp == data["temp"].max()])
#OR
# print(data[data.temp == data.temp.max()])


# to get the another data of the series where we know an another data of the row
# monday = data[data.day == "Monday"]
# print(monday.condition)


#print temperature in Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 +32
# print(monday_temp_F)


# Create a dataframe from scratch
# my_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(my_dict)
# new_data.to_csv("new_data.csv") # Takes argument of path of the file to be stored