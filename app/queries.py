import graphene
from .sqlalchemy_types import AuthorSQLType, BookSQLType
from .models import Author, Book
from sqlalchemy.orm import joinedload


class Query(graphene.ObjectType):

    authors = graphene.List(AuthorSQLType)

    books = graphene.List(BookSQLType)

    def resolve_authors(self, args, context, info):
        return Author.query.options(joinedload('books'), joinedload('books.readers')).all()

    def resolve_books(self, args, context, info):
        return Book.query.options(joinedload('readers')).all()
