"""empty message

Revision ID: c0f6912c8923
Revises: 
Create Date: 2018-11-19 09:51:19.884050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0f6912c8923'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
