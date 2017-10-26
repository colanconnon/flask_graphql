"""empty message

Revision ID: 33b9bd288b1b
Revises: 
Create Date: 2017-10-22 16:36:30.305602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33b9bd288b1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('isbn', sa.String(length=30), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_readers',
    sa.Column('books_id', sa.Integer(), nullable=True),
    sa.Column('readers_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['books_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['readers_id'], ['readers.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_readers')
    op.drop_table('books')
    op.drop_table('readers')
    op.drop_table('authors')
    # ### end Alembic commands ###
