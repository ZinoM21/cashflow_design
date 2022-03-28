"""update assets, add down payment

Revision ID: 333cbbe53b53
Revises: 3a1f6cbf51bc
Create Date: 2022-03-27 22:01:41.542024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333cbbe53b53'
down_revision = '3a1f6cbf51bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assets', sa.Column('down_payment', sa.Numeric(precision=10, scale=0), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assets', 'down_payment')
    # ### end Alembic commands ###