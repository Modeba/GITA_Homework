class User:
    def __init__(self, name = None, posts = None, friends = None):
        self.name = name
        self.posts = posts if posts is not None else []
        self.friends = friends if friends is not None else set()

user1 = User("Gio", ["A", "B"], set())
user2 = User("Levan")

user1.friends.add(user2)

print(user1.friends)