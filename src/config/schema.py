import graphene
import graphql_jwt
import gardens.schema
import beds.schema
import sections.schema
import users.schema


class Query(
    beds.schema.Query,
    gardens.schema.Query,
    sections.schema.Query,
    users.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    beds.schema.Mutation,
    gardens.schema.Mutation,
    sections.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
