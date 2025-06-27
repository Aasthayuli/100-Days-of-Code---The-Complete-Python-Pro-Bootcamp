import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


ran_index=random.randint(0,4)
print(friends[ran_index])

# OR

print(random.choice(friends))