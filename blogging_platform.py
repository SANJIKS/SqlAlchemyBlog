import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://django:1@localhost/blog_db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class BlogPost(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    created_at = Column(DateTime)

def create_post(title, content, author):
    session = Session()
    post = BlogPost(title=title, content=content, author=author)
    session.add(post)
    session.commit()
    session.close()

def get_post(post_id):
    session = Session()
    post = session.query(BlogPost).get(post_id)
    session.close()
    return post

def update_post(post_id, title, content):
    session = Session()
    post = session.query(BlogPost).get(post_id)
    if post:
        post.title = title
        post.content = content
        session.commit()
    session.close()

def delete_post(post_id):
    session = Session()
    post = session.query(BlogPost).get(post_id)
    if post:
        session.delete(post)
        session.commit()
    session.close()