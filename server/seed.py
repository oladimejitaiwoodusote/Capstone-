from app import app
from models import db, User, Record, Like, Comment
from flask_bcrypt import Bcrypt
from faker import Faker
from random import randint, choice as rc, sample

fake = Faker()
bcrypt = Bcrypt(app)

def create_users():
    users = []
    for _ in range(10):
        u = User(
            username = fake.user_name(),
            email = fake.email(),
            password = bcrypt.generate_password_hash("password").decode('utf-8')
        )
        users.append(u)

    return users

def create_records(users):
    records = []

    for _ in range(100):
        genres = ["Rock", "Hip-Hop", "Experimental", "Alternative"]
        images = ["https://upload.wikimedia.org/wikipedia/en/b/ba/Radioheadokcomputer.png", "https://upload.wikimedia.org/wikipedia/en/4/4b/My_Bloody_Valentine_-_Loveless.png", "https://upload.wikimedia.org/wikipedia/en/8/8a/Mmfood.jpg"]

        r = Record(
            title = fake.name(),
            artist = fake.name(),
            year = rc(range(1960,2023)),
            genre = rc(genres),
            cover_art = rc(images),
            user_id = rc([user.id for user in users])
        )
        records.append(r)
    return records

def create_likes(users, records):
    likes = []
    for _ in range(200):
        like = Like(
            user_id = rc([user.id for user in users]),
            record_id = rc([record.id for record in records])
        )
        likes.append(like)
    return likes

def create_comments(users, records):
    comments = []
    for _ in range(150):
        comment = Comment(
            text = fake.sentence(),
            user_id = rc([user.id for user in users]),
            record_id = rc([record.id for record in records])
        )
        comments.append(comment)
    return comments


if __name__ == "__main__":

    with app.app_context():
        User.query.delete()
        Record.query.delete()
        Like.query.delete()
        Comment.query.delete()
                              
        users = create_users()
        db.session.add_all(users)
        db.session.commit()
        #Make connections
        for u in users:
            temp = users
            temp.remove(u)
            u.following = sample(temp,randint(0,len(temp)-1))

        records = create_records(users)
        db.session.add_all(records)
        db.session.commit()

        likes = create_likes(users, records)
        db.session.add_all(likes)
        db.session.commit()

        comments = create_comments(users, records)
        db.session.add_all(comments)
        db.session.commit()