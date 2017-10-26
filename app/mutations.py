import graphene
from .types import AuthorType, BookType, ReaderInputType, ReaderType
from .models import Author, Book, Reader
from .app import db


class AuthorMutation(graphene.Mutation):

    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, args, context, info):
        author = Author.create(
            first_name=args['first_name'],
            last_name=args['last_name']
        )
        return AuthorMutation(author=author)


class BookMutation(graphene.Mutation):

    class Input:
        isbn = graphene.String(required=True)
        title = graphene.String(required=True)
        author_id = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(self, args, context, info):
        book = Book.create(
            title=args['title'],
            isbn=args['isbn'],
            author_id=args['author_id']
        )
        return BookMutation(book=book)


class AddReaderToBookMutation(graphene.Mutation):

    class Input:
        book_id = graphene.Int()
        reader = graphene.Argument(ReaderInputType)

    reader = graphene.Field(ReaderType)

    def mutate(self, args, context, info):
        reader = Reader.create(
            first_name=args['reader']['first_name'],
            last_name=args['reader']['last_name']
        )
        book = Book.get_by_id(args['book_id'])
        reader.books.append(book)
        reader.save()
        return AddReaderToBookMutation(reader=reader)


class Mutation(graphene.ObjectType):
    create_author = AuthorMutation.Field()
    create_book = BookMutation.Field()
    add_reader_to_book = AddReaderToBookMutation.Field()
