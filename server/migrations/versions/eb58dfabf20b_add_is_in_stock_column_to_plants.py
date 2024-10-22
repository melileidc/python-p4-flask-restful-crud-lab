"""Add is_in_stock column to plants

Revision ID: eb58dfabf20b
Revises: 0d27db194fc0
Create Date: 2024-10-11 12:54:03.828357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb58dfabf20b'
down_revision = '0d27db194fc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plants', sa.Column('is_in_stock', sa.Boolean(), nullable=True))
    op.alter_column('plants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('plants', 'price',
               existing_type=sa.FLOAT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plants', 'price',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('plants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('plants', 'is_in_stock')
    # ### end Alembic commands ###