import os
from xxlimited import new
from flask import Flask, jsonify, abort, request
from models import setup_db
from flask_cors import CORS
import sys

from models import setup_db, Actor, Movie

AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
ALGORITHMS = os.getenv('ALGORITHMS')
API_AUDIENCE = os.getenv('API_AUDIENCE')

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
        print("hi")
        print(AUTH0_DOMAIN)
        print(ALGORITHMS)
        print(API_AUDIENCE)
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

    # POST actors endpoint
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

    # POST movies endpoint
    @app.route('/movies', methods=['POST'])
    def create_movie():

        # Get new movie fields
        request_body = request.get_json()
        new_movie_title = request_body.get('title')
        new_movie_release_date = request_body.get('release_date')

        # Check for empty fields
        if new_movie_title == None or new_movie_title == "" or new_movie_release_date == None or new_movie_release_date == "":
            abort(400)

        try:
            # Create new movie
            new_movie = Movie(
                title=new_movie_title,
                release_date=new_movie_release_date,
            )

            # Add the new movie
            new_movie.insert()

            return jsonify({
                'success': True,
                'actor': new_movie.format()
            }), 201

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    # DELETE actors endpoint
    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        # Get the drink to be deleted
        actor = Actor.query.get(id)

        # Check if drink exists
        if actor is None:
            abort(404)

        try:
            # Delete drink
            actor.delete()

            return jsonify({
                'success': True,
                'delete': actor.id
            }), 200

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    # DELETE movies endpoint
    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movie(id):
        # Get the drink to be deleted
        movie = Movie.query.get(id)

        # Check if drink exists
        if movie is None:
            abort(404)

        try:
            # Delete drink
            movie.delete()

            return jsonify({
                'success': True,
                'delete': movie.id
            }), 200

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    # PATCH actors endpoint
    @app.route('/actors/<int:id>', methods=['PATCH'])
    def update_actor(id):

        # Get the drink to be updated
        actor = Actor.query.get(id)

        # Check if drink exists
        if actor is None:
            abort(404)

        try:
            # Get data to update
            request_body = request.get_json()

            if 'name' in request_body:
                actor.name = request_body['name']

            if 'age' in request_body:
                actor.age = request_body['age']

            if 'gender' in request_body:
                actor.gender = request_body['gender']

            # Update the drink
            actor.update()

            return jsonify({
                'success': True,
                'updated': actor.format()
            }), 200

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    # PATCH movies endpoint
    @app.route('/movies/<int:id>', methods=['PATCH'])
    def update_movie(id):

        # Get the drink to be updated
        movie = Movie.query.get(id)

        # Check if drink exists
        if movie is None:
            abort(404)

        try:
            # Get data to update
            request_body = request.get_json()

            if 'title' in request_body:
                movie.title = request_body['title']

            if 'release_date' in request_body:
                movie.release_date = request_body['release_date']


            # Update the drink
            movie.update()

            return jsonify({
                'success': True,
                'updated': movie.format()
            }), 200

        except Exception as err:
            print(f'Error: {err}')
            print(sys.exc_info())
            abort(500)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()