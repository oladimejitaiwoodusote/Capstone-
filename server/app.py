from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate  

from flask_bcrypt import Bcrypt

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = b'37bJJguZ0QHkrctykzGw0smKfRrYroIZ'

bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def get():
    return "1"

#Check if User is logged in
@app.get('/check_session')
def check_session():
    user_id = session.get("user_id")
    current_user = User.query.get(user_id)
    if current_user:
        return current_user.to_dict(), 200
    else:
        return {"message": "Not logged in"}, 401

#Log-In
@app.post('/login')
def login():
    json = request.json
    current_user = User.query.where(User.username == json['username']).first()
    if (current_user and bcrypt.check_password_hash(current_user.password, json['password'])):
        session['user_id'] = current_user.id
        return current_user.to_dict(), 201
    else:
        return {"message": "Invalid username or password"}, 401

#Create account
@app.post('/signup')
def signup():
    json = request.json
    pw_hash = bcrypt.generate_password_hash(json['password']).decode('utf-8')
    new_user = User(username=json["username"], email=json["email"], password = pw_hash)
    db.session.add(new_user)
    db.session.commit()
    session["user_id"] = new_user.id
    return new_user.to_dict(), 201

#Logout
@app.delete('/logout')
def logout():
    session.pop('user_id')
    return {}, 204

#Get users records based on user's ID
@app.get('/users_records/<int:id>')
def get_records(id):
    users_records = UsersRecord.query.where(UsersRecord.user_id == id).all()
    record_dicts = [record.record_details_to_dict() for record in users_records]
    return record_dicts, 200

@app.get('/comments/<int:id>')
def get_comments(id):
    comments = Comment.query.where(Comment.users_record_id == id).all()
    comment_dicts = [comment.to_dict() for comment in comments]
    return comment_dicts, 200   

#Add New Comment
@app.post('/comment')
def post_comment():
    json = request.json
    comment = Comment(text=json["text"], user_id=json["user_id"], users_record_id=json["record_id"])
    db.session.add(comment)
    db.session.commit()
    return comment.to_dict(), 201

#Add new record on profile page
@app.post('/record')
def post_record():
    json = request.json
    record = Record(title=json["title"], artist=json["artist"], year=json["year"], genre=json["genre"], cover_art=json["cover_art"])
    existing_record = Record.query.where(Record.title == record.title and Record.artist == record.artist).first()
    print(existing_record)
    if existing_record:
        new_user_record = UsersRecord(record_id = existing_record.id, user_id = session["user_id"])
        db.session.add(new_user_record)
        db.session.commit()
        return new_user_record.record_details_to_dict(), 201
    
    else:
        db.session.add(record)
        db.session.commit()
        new_record = Record.query.order_by(Record.id.desc()).first()
        user_record = UsersRecord(record_id = new_record.id, user_id = session["user_id"])
        db.session.add(user_record)
        db.session.commit()
        return user_record.record_details_to_dict(), 201

#Delete Record from profile page
@app.delete('/users_record/<int:id>')
def delete_record(id):
    users_record = UsersRecord.query.get(id)
    db.session.delete(users_record)
    db.session.commit()
    return f"{id}", 201

@app.patch('/record/<int:id>')
def edit_record(id):
    json = request.json
    record = Record.query.filter(Record.id == id).update(json)
    db.session.commit()
    record = Record.query.get(id)
    return record.to_dict(), 201

@app.get('/users/<int:id>')
def get_user_followersandfollowing(id):
    user = User.query.get(id)
    followers = user.followers
    followings = user.following
    follower_dicts = [follower.to_dict() for follower in followers]
    following_dicts = [following.to_dict() for following in followings]
    return {"followers": follower_dicts, "followings": following_dicts}, 201

#Get Feed
@app.get('/feed/<int:id>')
def get_feed(id):
    user = User.query.get(id)
    followings = user.following
    #users_records = UsersRecord.query.where(UsersRecord.user_id == id).all()
    followings_IDs = [user.id for user in followings]
    foll_collections = [UsersRecord.query.where(UsersRecord.user_id == i).all() for i in followings_IDs]
    follwings_dicts = [i.record_details_to_dict() for j in foll_collections for i in j]

    print(user)
    print(followings)
    print(followings_IDs)
    print(foll_collections)
    print(follwings_dicts)
    return follwings_dicts, 200

#Get user's details
@app.get('/users_details/<int:id>')
def get_user(id):
    user = User.query.get(id)
    print(user)
    return jsonify(user.to_dict()), 200

#Unfollow user
@app.get('/users_unfollow/<int:id>')
def unfollow_user(id):
    user = User.query.get(id)
    followers = user.followers
    user_id = session.get("user_id")
    currentUser = User.query.get(user_id)
    followers.remove(currentUser)
    db.session.commit()
    return currentUser.to_dict(), 201

#Follow user
@app.get('/users_follow/<int:id>')
def follow_user(id):
    user = User.query.get(id)
    followers = user.followers
    user_id = session.get("user_id")
    currentUser = User.query.get(user_id)
    followers.append(currentUser)
    db.session.commit()
    return currentUser.to_dict(), 201
    
if __name__ == "__main__":
    app.run(port=5555, debug=True)