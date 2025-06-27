states_of_america=["Delaware", "pencilvania", "New Jersey", "Georgia",
                   "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                   "New Hampshire", "Virginia", "New York", "North Carolina",
                   "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
                   "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                   "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                   "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                   "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                   "South Dakota", "Montana", "Washington", "Idaho", "Wyoming",
                   "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])
print(states_of_america[3])
print(states_of_america[4])


print()


# Prints the array in reverse
print(states_of_america[-1])
print(states_of_america[-2])
print(states_of_america[-3])
print(states_of_america[-4])


# Updating the array
states_of_america[1]="pennsylvania"
print("Updated Array")
print(states_of_america)

# Appending at the end of the list
states_of_america.append("new States")
print(states_of_america)


# extending the array by passing multiple items in the form of array or in square brackets
states_of_america.extend(["new state1","new state2","new state3"])



#list.append(x)
# list.extend(iterable)
# list.insert(i,x)
# list.remove(x)
# list.pop([i])
# list.clear()