""""added_k8s_node_table"

Revision ID: 44c50323f3bb
Revises: ceeab74f5036
Create Date: 2021-06-16 15:34:04.349090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44c50323f3bb'
down_revision = 'ceeab74f5036'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'k8s_node',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('cloud_account_id', sa.String(length=36), nullable=False),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=256), nullable=False),
        sa.Column('flavor', sa.String(length=256), nullable=True),
        sa.Column('provider_id', sa.String(length=256), nullable=True),
        sa.Column('hourly_price', sa.Float(), nullable=True),
        sa.Column('last_seen', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['cloud_account_id'], ['cloudaccount.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('cloud_account_id', 'name', 'provider_id', 'deleted_at',
                            name='uc_cloud_acc_id_name_provider_id_deleted_at')
    )


def downgrade():
    op.drop_table('k8s_node')
