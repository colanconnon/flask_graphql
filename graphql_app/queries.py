import graphene
from .sqlalchemy_types import AuthorSQLType, BookSQLType
from .models import Author, Book
from sqlalchemy.orm import joinedload, subqueryload
from flask_jwt_extended import get_jwt_identity
from graphql.utils.ast_to_dict import ast_to_dict
from flask import request
from .utils import get_optimized_joins
from sqlalchemy.orm import joinedload



class Query(graphene.ObjectType):

    authors = graphene.List(AuthorSQLType)

    books = graphene.List(BookSQLType)

    def resolve_authors(self, info):
        result = get_optimized_joins(Author, info)
        return Author.query.options(*result).all()

    def resolve_books(self, info):
        result = get_optimized_joins(Book, info)
        return Book.query.options(*result).all()
