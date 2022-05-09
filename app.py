import os
from flask import Flask, jsonify, abort
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

    return app

app = create_app()

if __name__ == '__main__':
    app.run()