from app import app
from models import db, User, Record, Like, Comment, UsersRecord
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

def create_records():
    records = [] 
    r1 = Record(title = "OK Computer", artist = "Radiohead", year = 1997, genre = "Art Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/b/ba/Radioheadokcomputer.png")
    r2 = Record(title = "To Pimp A Butterfly", artist = "Kendrick Lamar", year = 2015, genre = "Hip Hop", cover_art = "https://upload.wikimedia.org/wikipedia/en/f/f6/Kendrick_Lamar_-_To_Pimp_a_Butterfly.png")
    r3 = Record(title = "Unknown Pleasures", artist = "Joy Division", genre= "Post Punk", year = 1979, cover_art = "https://upload.wikimedia.org/wikipedia/en/5/5a/UnknownPleasuresVinyl.jpg")
    r4 = Record(title = "Madvillainy", artist = "Madvillain", year = 2004, genre = "Hip Hop", cover_art = "https://upload.wikimedia.org/wikipedia/en/5/5e/Madvillainy_cover.png")
    r5 = Record(title = "Mm..Food", artist="MF DOOM", year = 2004, genre="Hip Hop", cover_art = "https://upload.wikimedia.org/wikipedia/en/8/8a/Mmfood.jpg")
    r6 = Record(title = "Loveless", artist = "My Bloody Valentine", year = 1991, genre ="Shoegaze", cover_art = "https://upload.wikimedia.org/wikipedia/en/4/4b/My_Bloody_Valentine_-_Loveless.png")
    r7 = Record(title = "Slanted and Enchanted", artist = "Pavement", year = 1994, genre = "Indie Rock", cover_art = "https://upload.wikimedia.org/wikipedia/en/5/54/Slanted_and_Enchanted_album_cover.jpg")
    r8 = Record(title = "How To Leave Town", artist="Car Seat Headrest", year = 2014, genre = "Indie Rock", cover_art = "https://i.scdn.co/image/ab67616d0000b2730bebbf72e105d3ac60bd458d")
    
    records.append(r1)
    records.append(r2)
    records.append(r3)
    records.append(r4)
    records.append(r5)
    records.append(r6)
    records.append(r7)
    records.append(r8)

    # for _ in range(100):
    #     genres = ["Rock", "Hip-Hop", "Experimental", "Alternative"]
    #     images = ["https//upload.wikimedia.org/wikipedia/en/b/ba/Radioheadokcomputer.png", "https://upload.wikimedia.org/wikipedia/en/4/4b/My_Bloody_Valentine_-_Loveless.png", "https://upload.wikimedia.org/wikipedia/en/8/8a/Mmfood.jpg", "https://upload.wikimedia.org/wikipedia/en/e/e0/Twin_fantasy.jpg", "https://upload.wikimedia.org/wikipedia/en/6/60/Teens_of_Denial_Car_Seat_Headrest.jpg" ]

    #     r = Record(
    #         title = fake.name(),
    #         artist = fake.name(),
    #         year = rc(range(1960,2023)),
    #         genre = rc(genres),
    #         cover_art = rc(images),
    #     )
    #     records.append(r)
    return records

def create_users_records(users, records):
    users_records = []

    for _ in range(300):
        ur = UsersRecord(
            user_id = rc([user.id for user in users]),
            record_id = rc([record.id for record in records])
        )
        users_records.append(ur)
    return users_records

def create_likes(users, users_records):
    likes = []
    for _ in range(300):
        like = Like(
            user_id = rc([user.id for user in users]),
            users_record_id = rc([ur.id for ur in users_records])
        )
        likes.append(like)
    return likes

def create_comments(users, users_records):
    comments = []
    for _ in range(300):
        comment = Comment(
            text = fake.sentence(),
            user_id = rc([user.id for user in users]),
            users_record_id = rc([ur.id for ur in users_records])
        )
        comments.append(comment)
    return comments


if __name__ == "__main__":

    with app.app_context():
        User.query.delete()
        Record.query.delete()
        Like.query.delete()
        Comment.query.delete()
        UsersRecord.query.delete()
                              
        users = create_users()
        db.session.add_all(users)
        db.session.commit()
        #Make connections
        for u in users:
            temp = users
            temp.remove(u)
            u.following = sample(temp,randint(0,len(temp)-1))

        records = create_records()
        db.session.add_all(records)
        db.session.commit()

        users_records = create_users_records(users, records)
        db.session.add_all(users_records)
        db.session.commit()

        likes = create_likes(users, users_records)
        db.session.add_all(likes)
        db.session.commit()

        comments = create_comments(users, users_records)
        db.session.add_all(comments)
        db.session.commit()