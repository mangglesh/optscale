""""added_checklist_table"

Revision ID: 3a35cbdb4fe0
Revises: 865bb21cc4a4
Create Date: 2020-09-14 09:28:22.767969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a35cbdb4fe0'
down_revision = '865bb21cc4a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('checklist',
    sa.Column('deleted_at', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.String(length=36), nullable=False),
    sa.Column('last_run', sa.Integer(), nullable=False),
    sa.Column('next_run', sa.Integer(), nullable=False),
    sa.Column('last_completed', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['partner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('checklist')
    # ### end Alembic commands ###
