import unittest
from social_media import User, Post, Comment, Like


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        # Initialize a new user before each test
        self.user = User(username="test_user")

    def test_create_post_failure(self):
        # Create a new post with different content than expected
        expected_content = "This is the expected post content."
        post_content = "This is a test post."
        self.user.create_post(post_content)

        # Modify the assertions to expect failure
        self.assertEqual(len(self.user.posts), 1)
        self.assertEqual(self.user.posts[0].content, expected_content)

    def test_add_comment_to_post(self):
        # Create a post and add a comment to it
        post_content = "This is a test post."
        post = self.user.create_post(post_content)

        comment_content = "Test comment on the post."
        comment = Comment(author=self.user, content=comment_content)
        post.add_comment(comment)

        self.assertEqual(len(post.comments), 1)
        self.assertEqual(post.comments[0].content, comment_content)

    def test_like_post(self):
        # Create a post and like it
        post_content = "This is a test post."
        post = self.user.create_post(post_content)

        another_user = User(username="another_user")
        like = Like(user=another_user)
        post.add_like(like)

        self.assertEqual(post.likes_count(), 1)


if __name__ == '__main__':
    unittest.main()
