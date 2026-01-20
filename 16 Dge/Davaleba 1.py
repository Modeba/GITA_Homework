class User:
    def __init__(self, username, posts = None, friends = None):
        self.username = username
        self.posts = posts if posts else []
        self.friends = friends if friends else set()

    def add_friend(self, user):
        self.friends.add(user)
        user.friends.add(self)

    def make_post(self, content):
        post = Post(content, self)
        self.posts.append(post)

    def make_comment(self, content, post):
        comment = Comment(content, self)
        post.comments.append(comment)        

    def __repr__(self):
        return self.username
    
    def show_all_posts(self):
        return [post.content for post in self.posts]
    
class Post:
    def __init__(self, content, author, comments=None, likes=None):
        self.content = content
        self.author = author
        self.comments = comments if comments else []
        self.likes = likes if likes else []
    
    def __repr__(self):
        return f"{self.content}"

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author
    
    def __repr__(self):
        return f"{self.content}"


# Create 2 users
u1 = User('Ana')
u2 = User('Gio')

# Make them friends
u1.add_friend(u2)

# User 1 makes a post
u1.make_post('It is very sunny today')

# User 2 comments on the post
u2.make_comment('Nice weather', u1.posts[0])

