import graphene
from graphene_django import DjangoObjectType
from .models import Order

class OrderType(DjangoObjectType):
    
    class Meta:
        model = Order

    extra_field = graphene.String()

    def resolve_extra_field(self, info):
        return f"{self.id} : {self.name}"

class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)
    order = graphene.Field(OrderType, name=graphene.String())

    def resolve_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_order(self, info, name=None):
        return Order.objects.get(name=name)

class CreateOrder(graphene.Mutation):
    
    class Arguments:
        name = graphene.String()
    
    order = graphene.Field(OrderType)

    def mutate(self, info, name=None):
        order = Order.objects.create(
            name=name
        )
        return CreateOrder(order=order)

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()



    