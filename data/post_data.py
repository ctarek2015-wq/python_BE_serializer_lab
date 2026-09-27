from models.post import PostModel
from models.comment import CommentModel

# We create some instances of our tea model here, which will be used in seeding.
posts_list = [
    PostModel(title="First Post", content="This is the first post", author="Author1"),
    PostModel(title="Second Post", content="This is the second post", author="Author2"),
    PostModel(title="Third Post", content="This is the third post", author="Author3"),
    PostModel(title="Fourth Post", content="This is the fourth post", author="Author4"),
    PostModel(title="Fifth Post", content="This is the fifth post", author="Author5"),
    PostModel(title="Sixth Post", content="This is the sixth post", author="Author6"),
    PostModel(
        title="Seventh Post", content="This is the seventh post", author="Author7"
    ),
    PostModel(title="Eighth Post", content="This is the eighth post", author="Author8"),
    PostModel(title="Ninth Post", content="This is the ninth post", author="Author9"),
]

comments_list = [
    CommentModel(content="This is a great post", post_id=1),
    CommentModel(content="Perfect for relaxing evenings", post_id=2),
    CommentModel(content="I love the vibrant green color!", post_id=3),
    CommentModel(content="So refreshing and healthy!", post_id=4),
    CommentModel(content="A classic choice for any time of day", post_id=5),
]
