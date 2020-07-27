"""empty message

Revision ID: 6b5d871bd81f
Revises: 
Create Date: 2020-07-25 20:46:08.824760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b5d871bd81f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
