"""create Liabilities

Revision ID: 97d7e2d3d96a
Revises: 333cbbe53b53
Create Date: 2022-03-27 22:17:53.284278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d7e2d3d96a'
down_revision = '333cbbe53b53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('liabilitytypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('liability_type', sa.String(length=20, collation=0), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('liabilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20, collation=0), nullable=True),
    sa.Column('liability_type_id', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('payment', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.ForeignKeyConstraint(['liability_type_id'], ['liabilitytypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('liabilities')
    op.drop_table('liabilitytypes')
    # ### end Alembic commands ###