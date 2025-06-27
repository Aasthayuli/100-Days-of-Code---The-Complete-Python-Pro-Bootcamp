# class User:
#     pass
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "aasthayuli"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
#
# print(user_2.username)

# class User:
#     def __init__(self):
#         print("new user being created.")
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "aasthayuli"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
#
# print(user_2.username)



class User:
    def __init__(self, user_id, username):
        print("new user created.")
        self.id = user_id  # Attributes
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Aasthayuli")
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "Tanu Singh")
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

user_1.follow(user_2)
print("User1 followers: "+str(user_1.followers))
print("User2 followers: "+str(user_2.followers))
print("User1 following: "+str(user_1.following))
print("User2 following: "+str(user_2.following))