import click

from server.app import app
from server.models.meta import Base, engine
from server.models.channel import Channel
from server.models.member import Member
from server.models.messages import Message
from server.models.team import Team
from server.models.user import User


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


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
