""""clouds_nullable_fields"

Revision ID: 0f7376d5f910
Revises: cc8a74570004
Create Date: 2018-09-07 15:25:19.345934

"""
from alembic import op
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Session
from sqlalchemy import update, String
from sqlalchemy.sql import table, column
from cryptography.fernet import Fernet


# revision identifiers, used by Alembic.
revision = '0f7376d5f910'
down_revision = 'cc8a74570004'
branch_labels = None
depends_on = None


def _encrypt_password(password, salt):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet.encrypt((password + salt).encode())


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cloud', 'endpoint',
                    existing_type=String(256),
                    nullable=True)
    op.alter_column('cloud', 'password',
                    existing_type=sa.LargeBinary(),
                    nullable=True)
    op.alter_column('cloud', 'salt',
                    existing_type=String(256),
                    nullable=True)
    op.alter_column('cloud', 'username',
                    existing_type=String(256),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = Session(bind=bind)
    password = 'my-migration-pass'
    salt = str(uuid.uuid4())
    enc_password = _encrypt_password(password, salt)
    try:
        cloud_table = table('cloud',
                            column('username', String(256)),
                            column('id', String(36)),
                            column('salt', String(256)),
                            column('password', String(256)),
                            column('endpoint', String(256)))

        upd_stmt_name = update(cloud_table).values(
            username='username').where(
            cloud_table.c.username.is_(None))
        upd_stmt_salt = update(cloud_table).values(
            username=salt).where(
            cloud_table.c.salt.is_(None))
        upd_stmt_pass = update(cloud_table).values(
            password=enc_password).where(
            cloud_table.c.password.is_(None))
        upd_stmt_endpoint = update(cloud_table).values(
            endpoint='endpoint').where(
            cloud_table.c.endpoint.is_(None))
        for upd_stmt in [upd_stmt_name, upd_stmt_salt, upd_stmt_pass,
                         upd_stmt_endpoint]:
            session.execute(upd_stmt)
        session.commit()
    finally:
        session.close()
    op.alter_column('cloud', 'username',
                    existing_type=String(256),
                    nullable=False)
    op.alter_column('cloud', 'salt',
                    existing_type=String(256),
                    nullable=False)
    op.alter_column('cloud', 'password',
                    existing_type=sa.LargeBinary(),
                    nullable=False)
    op.alter_column('cloud', 'endpoint',
                    existing_type=String(256),
                    nullable=False)
    # ### end Alembic commands ###
