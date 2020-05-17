from app.views import message_blueprint

def init_app(app):
    app.register_blueprint(message_blueprint)