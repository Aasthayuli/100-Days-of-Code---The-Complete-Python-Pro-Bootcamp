# capitals = {
#     "France" : "Paris",
#     "Germany" : "berlin"
# }

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print lille
# print(travel_log["France"][1])


# Nested List
# nested_list = ["A", "B", ["C","D"]]
# print(nested_list[2])
# print(nested_list[2][1])

travel_log ={
    "France" : {
        "cities_visited" : ["Paris","Lille","Dijon"],
        "total_visits" :8,
    },
    "Germany" :{
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log)
print()
print(travel_log["France"])
print()
print(travel_log["France"]["total_visits"])
print()
print(travel_log["France"]["cities_visited"][1])
