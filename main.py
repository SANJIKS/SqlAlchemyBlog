from blogging_platform import create_post, get_post, update_post, delete_post


create_post("First post", "This is the content of my first post.", "John Doe")
create_post("Second post", "This is the content of my second post.", "Jane Smith")

post = get_post(1)
if post:
    print(f"Title: {post.title}")
    print(f"Content: {post.content}")
    print(f"Author: {post.author}")
    print(f"Created At: {post.created_at}")
else:
    print("Post not found.")

update_post(1, "Updated post", "This is the updated content of my first post.")

delete_post(2)