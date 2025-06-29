# TODO: to make a separate file for the colors of the squirrel

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
# print(gray_squirrel)

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# print("\nGray Squirrels: "+str(gray_squirrels_count))

Cinnamon_squirrel_count =len( data[data["Primary Fur Color"] == "Cinnamon"])
# print("\nCinnamon_squirrel Squirrels: "+str(Cinnamon_squirrel_count))

Black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print("\nBlack Squirrels: "+str(Black_squirrel_count))

data_dict= {
    "Fur Color" : ["Gray","Cinnamon", "Black"],
    "Count": [gray_squirrels_count, Cinnamon_squirrel_count, Black_squirrel_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")