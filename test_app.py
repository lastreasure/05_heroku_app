import unittest
import os
import json
from models import setup_db
from app import create_app
from flask_sqlalchemy import SQLAlchemy

# 0Auth tokens
assistant_token = os.environ['ASSISTANT_TOKEN']
director_token = os.environ['DIRECTOR_TOKEN']
producer_token = os.environ['PRODUCER_TOKEN']
database_path = os.environ['TEST_DATABASE_URL']

if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, database_path)
        self.casting_assistant = assistant_token
        self.casting_director = director_token
        self.executive_producer = producer_token
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()            
            # mock_data_insert()

    def tearDown(self):
        """Executed after reach test"""
        pass

    ##### Testing success of each endpoint

    def test_create_actor(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        new_actor = {
            "age": 22,
            "gender": "Female",
            "name": "Newest Actor"
        }
        res = self.client().post('/actors', json=new_actor, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_create_movie(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        new_movie = {
            "title": "New Movie",
            "release_date": "06-07-2009"
        }
        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
    
    def test_get_actors(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        res = self.client().get('/actors', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data.get('actors') != None)

    def test_get_movies(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data.get('movies') != None)

    def test_delete_actor(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        res = self.client().delete('/actors/58', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        res = self.client().delete('/movies/58', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        patched_actor = {'name': 'Updated New Actor'}
        res = self.client().patch('/actors/3', json=patched_actor, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        patched_movie = {'title': 'Updated New Movie'}
        res = self.client().patch('/movies/3', json=patched_movie, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ##### Testing error behaviour of each endpoint

    # misspelled compulsory name field
    def test_create_actor_fail(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        new_actor = {
            "na2nej2me": "Newest Actor",
            "age": 22,
            "gender": "Female",
        }
        res = self.client().post('/actors', json=new_actor, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    # missing compulsory title field 
    def test_create_movie_fail(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        new_movie = {
            "release_date": "06-07-2009"
        }
        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    # mispelled url
    def test_get_actors_fail(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        res = self.client().get('/actorss', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    # mispelled url
    def test_get_movies_fail(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        res = self.client().get('/moviess', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # non existant id
    def test_delete_actor_fail(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        res = self.client().delete('/actors/21321123', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # non existant id
    def test_delete_movie_fail(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        res = self.client().delete('/movies/5433433543', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # non existant id
    def test_update_actor_fail(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        patched_actor = {'name': 'Updated New Actor'}
        res = self.client().patch('/actors/43467832482', json=patched_actor, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # non existant title
    def test_update_movie_fail(self):
        headers = {'Authorization': f"Bearer {producer_token}"}
        patched_movie = {'tifdsfstle': "title"}
        res = self.client().patch('/movies/3', json=patched_movie, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    ##### Testing RBAC

    #  casting assistant cannot post, patch or delete
    def test_create_movie_RBAC_assistant_fail(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        new_movie = {
            "title": "New Movie",
            "release_date": "06-07-2009"
        }
        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_delete_movie_RBAC_assistant_fail(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        res = self.client().delete('/movies/1', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_update_actor_RBAC_assistant_fail(self):
        headers = {'Authorization': f"Bearer {assistant_token}"}
        patched_actor = {'name': 'Updated New Actor'}
        res = self.client().patch('/actors/3', json=patched_actor, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    #  casting director cannot post or delete movies
    def test_delete_movie_RBAC_director_fail(self):
        headers = {'Authorization': f"Bearer {director_token}"}
        res = self.client().delete('/movies/1', headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_create_movie_RBAC_director_fail(self):
        headers = {'Authorization': f"Bearer {director_token}"}
        new_movie = {
            "title": "New Movie",
            "release_date": "06-07-2009"
        }
        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
