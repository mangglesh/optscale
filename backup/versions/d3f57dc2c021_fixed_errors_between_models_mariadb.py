"""Fixed errors between models/mariadb

Revision ID: d3f57dc2c021
Revises: ea8a415c2999
Create Date: 2021-11-18 16:14:18.823265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3f57dc2c021'
down_revision = 'ea8a415c2999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_shareable_booking_resource_id'),
                    'shareable_booking', ['resource_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shareable_booking_resource_id'),
                  table_name='shareable_booking')
    # ### end Alembic commands ###
