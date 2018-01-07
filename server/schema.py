import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from server.models.channel import Channel
from server.models.member import Member
from server.models.messages import Message
from server.models.team import Team
from server.models.user import User


class Channel(SQLAlchemyObjectType):
    class Meta:
        model = Channel
        interfaces = (relay.Node, )


class Member(SQLAlchemyObjectType):
    class Meta:
        model = Member
        interfaces = (relay.Node, )


class Message(SQLAlchemyObjectType):
    class Meta:
        model = Message
        interfaces = (relay.Node, )


class Team(SQLAlchemyObjectType):
    class Meta:
        model = Team
        interfaces = (relay.Node, )


class User(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()


schema = graphene.Schema(query=Query)
