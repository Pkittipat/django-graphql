import graphene
import src.order.schema
class Query(src.order.schema.Query, graphene.ObjectType):
    pass

class Mutation(src.order.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)