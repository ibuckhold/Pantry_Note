"""empty message

Revision ID: f850722e6d85
Revises: 570ad9677d9b
Create Date: 2021-05-07 15:27:38.447546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f850722e6d85'
down_revision = '570ad9677d9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeName', sa.String(length=50), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('instructions', sa.Text(), nullable=False),
    sa.Column('estimatedTime', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('recipeName')
    )
    op.create_table('pantry_ingredients',
    sa.Column('ingredientsId', sa.Integer(), nullable=True),
    sa.Column('pantryId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredientsId'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['pantryId'], ['pantries.id'], )
    )
    op.create_table('recipe_ingredients',
    sa.Column('ingredientsId', sa.Integer(), nullable=True),
    sa.Column('recipeId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredientsId'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recipeId'], ['recipies.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredients')
    op.drop_table('pantry_ingredients')
    op.drop_table('recipies')
    # ### end Alembic commands ###
