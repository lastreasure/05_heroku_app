"""empty message

Revision ID: 0a457bc1150a
Revises: 96f1e730812a
Create Date: 2022-05-09 18:06:54.061445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a457bc1150a'
down_revision = '96f1e730812a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actors', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('actors', 'age')
    # ### end Alembic commands ###
