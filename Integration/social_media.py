class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = Post(author=self, content=content)
        self.posts.append(post)
        return post

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []
        self.likes = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, like):
        self.likes.append(like)

    def likes_count(self):
        return len(self.likes)

class Comment:
    def __init__(self, author, content):
        self.author = author
        self.content = content

class Like:
    def __init__(self, user):
        self.user = user
