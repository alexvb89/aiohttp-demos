import graphene

from graph.api.mutations.messages import (
    AddMessageMutation,
    RemoveMessageMutation,
)


class Mutation(graphene.ObjectType):
    '''
    The main GraphQL mutation point.
    '''

    add_message = AddMessageMutation.Field()
    remove_message = RemoveMessageMutation.Field()
