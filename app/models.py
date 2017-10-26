# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt
from .database import Column, Model, SurrogatePK, db, reference_col, relationship


class Author(SurrogatePK, Model):

    __tablename__ = 'authors'
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    created_at = Column(db.DateTime, nullable=False,
                        default=dt.datetime.utcnow)


book_reader_association_table = db.Table('book_readers', db.metadata,
                                         Column('books_id', db.Integer,
                                                db.ForeignKey('books.id')),
                                         Column('readers_id', db.Integer,
                                                db.ForeignKey('readers.id'))
                                         )


class Book(SurrogatePK, Model):
    __tablename__ = 'books'
    title = Column(db.String(50), nullable=False)
    isbn = Column(db.String(30), nullable=False)
    author_id = reference_col('authors', nullable=False)
    author = relationship('Author', backref='books')
    readers = relationship(
        "Reader",
        secondary=book_reader_association_table,
        back_populates="books")


class Reader(SurrogatePK, Model):
    __tablename__ = 'readers'
    first_name = Column(db.String(50), nullable=False)
    last_name = Column(db.String(50), nullable=False)
    books = relationship(
        "Book",
        secondary=book_reader_association_table,
        back_populates="readers")
