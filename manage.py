from server.app import app
from server.models.meta import Base, engine
from server import models


@app.cli.command()
def init_db():
    """Initalize the database."""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
