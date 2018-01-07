import click
from flask import Flask
from flask_graphql import GraphQLView

from server.models.meta import Base, engine, session

from server.models.channel import Channel
from server.models.member import Member
from server.models.messages import Message
from server.models.team import Team
from server.models.user import User

from server.schema import schema


app = Flask(__name__)

app.config.from_object("server.settings")

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


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
    session.remove()


@app.route("/")
def root():
    return {}
