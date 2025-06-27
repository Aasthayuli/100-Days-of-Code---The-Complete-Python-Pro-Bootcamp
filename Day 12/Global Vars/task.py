# Modifying Global Scope

enemies = "Skeleton"


def increase_enemies():
    global enemies  # to modify the global variable
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


