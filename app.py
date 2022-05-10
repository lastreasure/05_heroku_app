import os
from xxlimited import new
from flask import Flask, jsonify, abort, request
from models import setup_db
from flask_cors import CORS
import sys

from models import setup_db, Actor, Movie

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # Using the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
        return jsonify({
            'message': 'Hello this is the Casting Agency Models Company website',
            'success': True,
        }), 200

    # GET actors endpoint
    @app.route('/actors')
    def get_actors():
        try:
            actors_list = Actor.query.all()

            if actors_list == 0:
                abort(404)

            return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors_list]
        }), 200

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    # GET movies endpoint
    @app.route('/movies')
    def get_movies():
        try:
            movies_list = Movie.query.all()

            if movies_list == 0:
                abort(404)

            return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies_list]
        }), 200

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    # GET actors endpoint
    @app.route('/actors', methods=['POST'])
    def create_actor():

        # Get new actor fields
        request_body = request.get_json()
        new_actor_name = request_body.get('name')
        new_actor_age = request_body.get('age')
        new_actor_gender = request_body.get('gender')

        # Check for empty fields
        if new_actor_name == None or new_actor_name == "":
            abort(400)

        try:
            # Create new actor
            new_actor = Actor(
                name=new_actor_name,
                age=new_actor_age,
                gender=new_actor_gender,
            )

            # Add the new actor
            new_actor.insert()

            return jsonify({
                'success': True,
                'actor': new_actor.format()
            }), 201

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)



    return app

app = create_app()

if __name__ == '__main__':
    app.run()