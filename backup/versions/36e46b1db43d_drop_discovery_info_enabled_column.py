""""drop_discovery_info_enabled_column"

Revision ID: 36e46b1db43d
Revises: 8f9717cc2d71
Create Date: 2021-11-18 15:20:31.570518

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

# revision identifiers, used by Alembic.

revision = '36e46b1db43d'
down_revision = '8f9717cc2d71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('discovery_info', 'enabled')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('discovery_info', sa.Column('enabled', sa.Boolean(),
                                              default=True, nullable=False))
    di_table = sa.table('discovery_info', sa.Column(
        'enabled', sa.Boolean(), nullable=False))
    bind = op.get_bind()
    session = Session(bind=bind)
    enable_update = sa.update(di_table).values(enabled=True)
    try:
        session.execute(enable_update)
        session.commit()
    finally:
        session.close()
