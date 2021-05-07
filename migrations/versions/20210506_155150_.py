"""empty message

Revision ID: 570ad9677d9b
Revises: 67ea5987382c
Create Date: 2021-05-06 15:51:50.180955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '570ad9677d9b'
down_revision = '67ea5987382c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pantries', sa.Column('userId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pantries', 'users', ['userId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pantries', type_='foreignkey')
    op.drop_column('pantries', 'userId')
    # ### end Alembic commands ###