game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)  # doesn't cause error but is not a good practice.

# coz code blocks like if, while, for, etc.
# all of these with colons and indentation, they don't count as creating a local scope


# but a function creates a local scope
# print(new_enemy)      # causes error