import os
from xxlimited import new
from flask import Flask, jsonify, abort, request
from models import setup_db
from flask_cors import CORS
import sys
from auth import AuthError, requires_auth

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
    @requires_auth('get:actors')
    def get_actors(jwt):
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
    @requires_auth('get:movies')
    def get_movies(jwt):
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
    @requires_auth('post:actors')
    def create_actor(jwt):

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
    @requires_auth('post:movies')
    def create_movie(jwt):

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
    @requires_auth('delete:actors')
    def delete_actor(jwt, id):
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
    @requires_auth('delete:movies')
    def delete_movie(jwt, id):
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
    @requires_auth('patch:actors')
    def update_actor(jwt, id):

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
    @requires_auth('patch:movies')
    def update_movie(jwt, id):

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

    ### ERROR HANDLING ###
    @app.errorhandler(404)
    def unprocessable(err):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404

    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Client Error: Bad Request'
        }), 400

    @app.errorhandler(405)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405


    @app.errorhandler(422)
    def unproccessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unproccessable'
        }), 422


    @app.errorhandler(500)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.debug = True
    app.run()