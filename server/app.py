import click
from flask import Flask
from flask_graphql import GraphQLView

from server import model
from server.model.meta import Base, engine, session

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
            model.Channel.__table__,
            model.Member.__table__,
            model.Message.__table__,
            model.Team.__table__,
            model.User.__table__,
        ])

    Base.metadata.create_all()


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


@app.route("/")
def root():
    return {}
