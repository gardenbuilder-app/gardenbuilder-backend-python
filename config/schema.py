import graphene
import graphql_jwt
import apps.gardens.schema
import apps.beds.schema
import apps.sections.schema
import apps.users.schema


class Query(
    apps.beds.schema.Query,
    apps.gardens.schema.Query,
    apps.sections.schema.Query,
    apps.users.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    apps.beds.schema.Mutation,
    apps.gardens.schema.Mutation,
    apps.sections.schema.Mutation,
    apps.users.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token = graphql_jwt.DeleteRefreshTokenCookie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
