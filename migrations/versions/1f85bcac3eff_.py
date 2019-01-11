"""empty message

Revision ID: 1f85bcac3eff
Revises: 94d5a07bdb22
Create Date: 2019-01-08 23:33:12.581398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f85bcac3eff'
down_revision = '94d5a07bdb22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_banned', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_banned')
    # ### end Alembic commands ###
