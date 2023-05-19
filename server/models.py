from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

user_follows=db.Table(
    "user_follows",
    db.Column('user_id', db.Integer, db.ForeignKey("users.id")),
    db.Column('following_id', db.Integer, db.ForeignKey("users.id"))
)

#Add Validations

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    records = db.relationship("Record", backref = "user")
    likes = db.relationship("Like", backref="user")
    comments = db.relationship("Comment", backref = "user")

    
    following = db.relationship(
        "User", lambda: user_follows,
        primaryjoin = lambda : User.id == user_follows.c.user_id,
        secondaryjoin = lambda: User.id == user_follows.c.following_id,
        backref = "followers"
    )

    def __repr__(self):
        return f"<User username={self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

class Record(db.Model):

    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String, nullable=False)
    cover_art = db.Column(db.String, nullable = False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    likes = db.relationship("Like", backref="record")
    comments = db.relationship("Comment", backref = "record")

    def __repr__(self):
        return f"<Record id={self.id} title={self.title} artist={self.artist} year={self.year} genre={self.genre}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "genre": self.genre,
            "cover_art": self.cover_art
        }

class Like(db.Model):

    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    record_id = db.Column(db.Integer, db.ForeignKey("records.id"))

    def __repr__(self):
        return f"<Like id={self.id}>"

    def to_dict(self):
        return {
            "id": self.id
        }

class Comment(db.Model):

    __tablename__= "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    record_id = db.Column(db.Integer, db.ForeignKey("records.id"))
    
    def __repr__(self):
        return f"<Comment id={self.id} text={self.text}>"

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "user":self.user.username
        }