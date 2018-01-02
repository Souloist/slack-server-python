from flask import Flask

from server.models import meta

app = Flask(__name__)

app.config.from_object("server.settings")


@app.teardown_appcontext
def shutdown_session(exception=None):
    meta.session.remove()


@app.route("/")
def root():
    return {}
