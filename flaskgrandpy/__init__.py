"""Flask app"""
import os

from flask import Flask

from flaskgrandpy import grandpy


def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(
        __name__,
        instance_relative_config=True
    )
    app.config.from_mapping(
        SECRET_KEY='dev' # TO CHANGE WHEN DEPLOYING TO PRODUCTION
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile(
            'config.py',
            silent=True
        )
    else:
        # Load the test config is passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # GrandPy page
    app.register_blueprint(grandpy.bp)
    app.add_url_rule('/', endpoint='index')

    return app
