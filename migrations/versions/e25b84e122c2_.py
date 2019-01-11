"""empty message

Revision ID: e25b84e122c2
Revises: f09b8d54118a
Create Date: 2019-01-08 17:10:58.668625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e25b84e122c2'
down_revision = 'f09b8d54118a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['commenter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'commenter_id')
    # ### end Alembic commands ###
