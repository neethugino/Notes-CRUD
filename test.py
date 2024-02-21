import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, db
from models import User

class TestYourApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_signup(self):
        response = self.client.post('/signup', json={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.query.filter_by(username='testuser').count(), 1)

    def test_user_login(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)

    # Add more tests for other routes and functionalities

if __name__ == '__main__':
    unittest.main()
