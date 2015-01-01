__author__ = 'hamid'

# import flask
from flask import Flask

# import project
from config import Config


def create_app(config=None, name='WWW'):
    app = Flask(name)

    configure_app(app, config)
    configure_blueprints(app)
    configure_errorhandlers(app)
    configure_before_handlers(app)
    configure_extentions(app)
    return app


def configure_app(app, config):
    # default config default
    app.config.from_object(Config())

    if config is not None:
        # add more config
        app.config.from_object(config)

    # if environment variable is set
    app.config.from_envvar('project_CONFIG', silent=True)


def configure_blueprints(app):

    blueprints = Config.INSTALLED_BLUEPRINTS
    for blueprint in blueprints:
        bp = __import__('app.blueprints.%s' % blueprint, fromlist=[blueprint])
        app.register_blueprint(bp.mod)


def configure_errorhandlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return "", 404

    @app.errorhandler(403)
    def forbidden(error):
        return "", 403

    @app.errorhandler(500)
    def internal_error(error):
        return "", 500


def configure_before_handlers(app):
    pass


def configure_extentions(app):
    from extensions import db
    db.init_app(app)