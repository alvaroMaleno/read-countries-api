from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.countries.get_routes import get_countries_bp
    app.register_blueprint(get_countries_bp)

    @app.route('/hc/')
    def hc_page():
        return '<h1>Healthy</h1>'

    return app
