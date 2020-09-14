import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        description = " Type definition for a single garden "

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, password, email):
        user = get_user_model()(
            email=email,
        )
        user.set_password(password)
        print(user)
        user.save()

        return CreateUser(user=user)


class Query(graphene.AbstractType):
    current_user = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()
    
    def resolve_current_user(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in!")
        return user


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
