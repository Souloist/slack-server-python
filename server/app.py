import click
from flask import Flask

from server.models import meta
from server.models.meta import Base, engine
from server.models.channel import Channel
from server.models.member import Member
from server.models.messages import Message
from server.models.team import Team
from server.models.user import User


app = Flask(__name__)

app.config.from_object("server.settings")


@app.cli.command()
@click.option("--drop", default=False)
def initdb(drop):
    """Initalize the database."""
    Base.metadata.bind = engine

    if drop:
        Base.metadata.drop_all(tables=[
            Channel.__table__,
            Member.__table__,
            Message.__table__,
            Team.__table__,
            User.__table__,
        ])

    Base.metadata.create_all()


@app.teardown_appcontext
def shutdown_session(exception=None):
    meta.session.remove()


@app.route("/")
def root():
    return {}
