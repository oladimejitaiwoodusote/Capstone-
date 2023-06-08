from app import app
from models import db, User, Record, Like, Comment, UsersRecord
from flask_bcrypt import Bcrypt
from faker import Faker
from random import randint, choice as rc, sample

fake = Faker()
bcrypt = Bcrypt(app)

def create_users():
    avatars = ["https://d7hftxdivxxvm.cloudfront.net/?height=800&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FqNzvYZT0RbuuyuSyrs6wWw%2Fnormalized.jpg&width=719",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Elliott_Smith.jpg/440px-Elliott_Smith.jpg", 
     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/MF_Doom_-_Hultsfred_2011_%28cropped%29.jpg/440px-MF_Doom_-_Hultsfred_2011_%28cropped%29.jpg",
     "https://pbs.twimg.com/media/DaT9nhjX4AAiKW-.jpg",
     "https://news.artnet.com/app/news-upload/2014/06/bjork-app-moma-acquisition.jpg",
     "https://pbs.twimg.com/media/EmO-CcJXEAEOrV5.jpg"
     ]
    users = []
    for _ in range(30):
        u = User(
            username = fake.user_name(),
            email = fake.email(),
            password = bcrypt.generate_password_hash("password").decode('utf-8'),
            avatar = rc(avatars)
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
    r9 = Record(title = "Kid A", artist = "Radiohead", year = 2000, genre = "Post Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/0/02/Radioheadkida.png")
    r10 = Record(title = "In Rainbows", artist = "Radiohead", year = 2007, genre = "Art Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/1/14/Inrainbowscover.png")
    r11 = Record(title = "The Low End Theory", artist = "A Tribe Called Quest", year = 1991, genre = "Hip Hop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/4/42/ATribeCalledQuestTheLowEndtheory.jpg")
    r12 = Record(title = "Midnight Marauders", artist = "A Tribe Called Quest", year = 1993, genre = "Hip Hop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/1/16/ATCQMidnightMarauders.jpg")
    r13 = Record(title = "Liquid Swordz", artist = "GZA", year = 1995, genre = "Hip Hop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/9/90/Liquidswords1995.png")
    r14 = Record(title = "Magical Mystery Tour", artist = "The Beatles", year = 1995, genre = "Psychedelic Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/e/e8/MagicalMysteryTourDoubleEPcover.jpg")
    r15 = Record(title = "Slanted and Enchanted", artist = "Pavement", year = 1992, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/5/54/Slanted_and_Enchanted_album_cover.jpg")
    r16 = Record(title = "Crooked Rain Crooked Rain", artist = "Pavement", year = 1994, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/6/64/Pavement_Crooked_Rain.jpg")
    r17 = Record(title = "Perfect From Now On", artist = "Built to Spill", year = 1997, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/0/08/Perfect_From_Now_On.jpg")
    r18 = Record(title = "Teens of Denial", artist = "Car Seat Headrest", year = 2015, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/6/60/Teens_of_Denial_Car_Seat_Headrest.jpg")
    r19 = Record(title = "Emergency & I", artist = "The Dismemberment Plan", year = 1999, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Emergency_%26_I.jpg/440px-Emergency_%26_I.jpg")
    r20 = Record(title = "Either/Or", artist = "Elliott Smith", year = 1997, genre = "Indie Folk", cover_art =  "https://upload.wikimedia.org/wikipedia/en/f/fd/Elliottsmitheitheror55.jpg")
    r21 = Record(title = "Elliott Smith", artist = "Elliott Smith", year = 1995, genre = "Indie Folk", cover_art =  "https://upload.wikimedia.org/wikipedia/en/e/e3/Elliott_Smith_%28album%29.jpg")
    r22 = Record(title = "XO", artist = "Elliott Smith", year = 1998, genre = "Indie Folk", cover_art =  "https://upload.wikimedia.org/wikipedia/en/3/35/ElliottsmithXOalbumcover.jpg")
    r23 = Record(title = "This is a Long Drive for Someone with Nothing to Think About", artist = "Modest Mouse", year = 1996, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/5/5b/MMLongDrive5075.jpg")
    r24 = Record(title = "The Lonesome Crowded West", artist = "Modest Mouse", year = 1997, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/f/f5/MMLonesomeCrowdedWest.jpg")
    r25 = Record(title = "Hounds of Love", artist = "Kate Bush", year = 1985, genre = "Art Pop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/3/3f/Katebushhoundsoflove.png")
    r26 = Record(title = "Funeral", artist = "Arcade Fire", year = 2004, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/2/25/ArcadeFireFuneralCover.jpg")
    r26 = Record(title = "The Suburbs", artist = "Arcade Fire", year = 2010, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/8/81/Arcade_Fire_-_The_Suburbs.jpg")
    r27 = Record(title = "Shields", artist = "Grizzly Bear", year = 2012, genre = "Indie Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/a/af/GrizzlyBearShields.jpg")
    r28 = Record(title = "Bloom", artist = "Beach House", year = 2012, genre = "Dream Pop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/a/a2/Beach_House_-_Bloom.png")
    r29 = Record(title = "Tean Dream", artist = "Beach House", year = 2010, genre = "Dream Pop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/b/b2/Beach_House_-_Teen_Dream.png")
    r30 = Record(title = "Vespertine", artist = "Bjork", year = 2001, genre = "Art Pop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/1/14/Bj%C3%B6rk_-_Vespertine_album_cover.png")
    r31 = Record(title = "Remain in Light", artist = "Talking Heads", year = 1980, genre = "Art Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/2/2d/TalkingHeadsRemaininLight.jpg")
    r32 = Record(title = "Blonde on Blonde", artist = "Bob Dylan", year = 1966, genre = "Folk Rock", cover_art =  "https://upload.wikimedia.org/wikipedia/en/3/38/Bob_Dylan_-_Blonde_on_Blonde.jpg")
    r32 = Record(title = "Fetch the Bolt Cutters", artist = "Fiona Apple", year = 2020, genre = "Art Pop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/0/00/Fiona_Apple_-_Fetch_the_Bolt_Cutters.png")
    r33 = Record(title = "Illmatic", artist = "Nas", year = 1994, genre = "Hip Hop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/2/27/IllmaticNas.jpg")
    r34 = Record(title = "ATLiens", artist = "Outkast", year = 1996, genre = "Hip Hop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/c/c6/Outkast-atliens.jpg")
    r35 = Record(title = "Aquemini", artist = "Outkast", year = 1998, genre = "Hip Hop", cover_art =  "https://upload.wikimedia.org/wikipedia/en/2/2c/AqueminiOutKast.jpg")


    
    records.append(r1)
    records.append(r2)
    records.append(r3)
    records.append(r4)
    records.append(r5)
    records.append(r6)
    records.append(r7)
    records.append(r8)
    records.append(r9)
    records.append(r10)
    records.append(r11)
    records.append(r12)
    records.append(r13)
    records.append(r14)
    records.append(r15)
    records.append(r15)
    records.append(r16)
    records.append(r17)
    records.append(r18)
    records.append(r19)
    records.append(r20)
    records.append(r21)
    records.append(r22)
    records.append(r23)
    records.append(r24)
    records.append(r25)
    records.append(r26)
    records.append(r27)
    records.append(r28)
    records.append(r29)
    records.append(r30)
    records.append(r31)
    records.append(r32)
    records.append(r33)
    records.append(r34)
    records.append(r35)

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
    for _ in range(600):
        like = Like(
            user_id = rc([user.id for user in users]),
            users_record_id = rc([ur.id for ur in users_records])
        )
        likes.append(like)
    return likes

def create_comments(users, users_records):
    #fake_comments = ["Awesome!", "These are all fake comments", "I am lying to you", "Awful album", "Overrated"]
    comments = []
    for _ in range(300):
        comment = Comment(
            text = fake.sentence(),
            #text = rc(fake_comments),
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
            # temp = users
            # temp.remove(u)
            u.following = sample(users,randint(0,len(users)-1))

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