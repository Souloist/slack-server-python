# Slack Clone Backend

Slack clone written in Python3 using the following:
* Sqlalchemy
* Flask
* GraphQL

Basically just wanted to check out graphQL. Yeah its overkill.

# Setup Notes

This project assumes you have a database called `slack`. If you have PostgreSQL installed you can create a database with `createdb slack`

```
export FLASK_APP=server/app.py
flask run
```

If you wish to develop and want debug mode enabled, you can add the environment variable `FLASK_DEBUG=1`
