import graphene
from .sqlalchemy_types import AuthorSQLType, BookSQLType
from .models import Author, Book
from sqlalchemy.orm import joinedload, subqueryload
from flask_jwt_extended import get_jwt_identity
from graphql.utils.ast_to_dict import ast_to_dict
from flask import request


def get_selections(ast):
    edges = []
    nodes = []
    print(ast_to_dict(ast))
    selections = ast.selection_set.selections
    for s in selections:
        if s.selection_set is None:
            edges.append(ast.name.value + '.' + s.name.value)
        else:
            nodes.append(s.name.value)
            t_edges, t_nodes = get_selections(s)
            edges = edges + t_edges
            nodes = nodes + t_nodes
    return edges, nodes


class Query(graphene.ObjectType):

    authors = graphene.List(AuthorSQLType)

    books = graphene.List(BookSQLType)

    def resolve_authors(self, info):
        join_look_up = {
            'books': joinedload('books'),
            'readers': joinedload('books.readers')
        }
        print(info.context)
        print(request)
        user = get_jwt_identity()
        ast = info.field_asts[0]
        edges, nodes = get_selections(ast)
        joins = []
        for node in nodes:
            joins.append(join_look_up[node])
        return Author.query.options(*joins).all()

    def resolve_books(self, info):
        return Book.query.options(joinedload('readers')).all()
