import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import get_token
import graphql_jwt
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        description = " Type definition for a single garden "

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    class Arguments:
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, password, email):
        user = get_user_model()(
            email=email,
        )
        user.set_password(password)
        user.save()
        user_token = get_token(user)

        return CreateUser(user=user,token=user_token)


class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        user = info.context.user
        if user.is_superuser:
            return get_user_model().objects.all()
        raise Exception("You must be a superuser to view other user's data")
        
    
    def resolve_current_user(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in!")
        return user


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
