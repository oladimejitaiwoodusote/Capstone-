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

@app.get('/check_session')
def check_session():
    user_id = session.get("user_id")
    current_user = User.query.get(user_id)
    if current_user:
        return current_user.to_dict(), 200
    else:
        return {"message": "Not logged in"}

@app.post('/login')
def login():
    json = request.json
    current_user = User.query.where(User.username == json['username']).first()
    if (current_user and bcrypt.check_password_hash(current_user.password, json['password'])):
        session['user_id'] = current_user.id
        return current_user.to_dict(), 201
    else:
        return {"message": "Invalid username or password"}, 401

@app.post('/signup')
def signup():
    json = request.json
    pw_hash = bcrypt.generate_password_hash(json['password']).decode('utf-8')
    new_user = User(username=json["username"], email=json["email"], password = pw_hash)
    db.session.add(new_user)
    db.session.commit()
    session["user_id"] = new_user.id
    return new_user.to_dict(), 201

@app.get('/users_records/<int:id>')
def get_records(id):
    records = Record.query.where(Record.user_id == id).all()
    record_dicts = [record.to_dict() for record in records]
    return record_dicts, 200

@app.get('/comments/<int:id>')
def get_comments(id):
    comments = Comment.query.where(Comment.record_id == id).all()
    comment_dicts = [comment.to_dict() for comment in comments]
    return comment_dicts, 200   

@app.post('/comment')
def post_comment():
    json = request.json
    comment = Comment(text=json["text"], user_id=json["user_id"], record_id=json["record_id"])
    db.session.add(comment)
    db.session.commit()
    return comment.to_dict(), 201
    



if __name__ == "__main__":
    app.run(port=5555, debug=True)