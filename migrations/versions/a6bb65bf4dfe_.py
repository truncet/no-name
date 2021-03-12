"""empty message

Revision ID: a6bb65bf4dfe
Revises: 26475a94339d
Create Date: 2021-03-10 19:20:14.731375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6bb65bf4dfe'
down_revision = '26475a94339d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=500), nullable=True))
    op.add_column('user', sa.Column('password', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('phone', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('profession', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profession')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'password')
    op.drop_column('user', 'location')
    op.drop_column('user', 'email')
    op.drop_column('user', 'age')
    # ### end Alembic commands ###