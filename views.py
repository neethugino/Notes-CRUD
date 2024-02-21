from flask import Flask, jsonify, request
from app import app,db
from models import User, Note, SharedNote
import hashlib


# Routes
    
@app.route('/')
def home():
    return 'Welcome to the Note-taking App!'

#Create a single user sign up view
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
    new_user = User(username=data['username'], password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User created successfully'}, 201

#Create a simple login view
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Hash the provided password
    password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
   
    # Check if the user exists and the password matches
    user = User.query.filter_by(username=data['username'], password=password_hash).first()
    
    if user:
        return {'message': 'Login successful'}, 200
    else:
        return {'message': 'Invalid credentials'}, 401
    

#create notes
@app.route('/notes/create', methods=['POST'])
def create_note():
    data = request.get_json()
    new_note = Note(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(new_note)
    db.session.commit()
    return {'message': 'Note created successfully'}, 201

#Retrieve and update specific note by its ID.
@app.route('/notes/<int:note_id>', methods=['GET', 'PUT'])
def get_or_update_note(note_id):
    note = Note.query.get(note_id)
    if not note:
        return {'message': 'Note not found'}, 404

    if request.method == 'GET':
        return {'id': note.id, 'title': note.title, 'content': note.content, 'user_id': note.user_id}, 200
    elif request.method == 'PUT':
        data = request.get_json()
        note.title = data['title']
        note.content = data['content']
        db.session.commit()
        return {'message': 'Note updated successfully'}, 200

#share to specific notes
@app.route('/notes/share', methods=['POST'])
def share_note():
    data = request.get_json()
    shared_note = SharedNote(note_id=data['note_id'], user_id=data['user_id'])
    db.session.add(shared_note)
    db.session.commit()
    return {'message': 'Note shared successfully'}, 201

#GET all the changes associated
@app.route('/notes/version-history/<int:id>', methods=['GET'])
def get_version_history(id):
    note = Note.query.get(id)
    if note:
        # Assuming you have a 'title' field in your Note model
        versions = Note.query.filter_by(title=note.title).all()

        # Create a list of dictionaries representing the versions
        version_list = [{'id': version.id, 'content': version.content} for version in versions]

        # Return the version history as JSON
        return jsonify({'version_history': version_list})
    else:
        return jsonify({'message': 'Note not found'}), 404

