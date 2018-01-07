import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from server import model as db_model


class Channel(SQLAlchemyObjectType):
    class Meta:
        model = db_model.Channel
        interfaces = (relay.Node, )


class Member(SQLAlchemyObjectType):
    class Meta:
        model = db_model.Member
        interfaces = (relay.Node, )


class Message(SQLAlchemyObjectType):
    class Meta:
        model = db_model.Message
        interfaces = (relay.Node, )


class Team(SQLAlchemyObjectType):
    class Meta:
        model = db_model.Team
        interfaces = (relay.Node, )


class User(SQLAlchemyObjectType):
    class Meta:
        model = db_model.User
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()


schema = graphene.Schema(query=Query)
