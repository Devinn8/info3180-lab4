"""empty message

Revision ID: 352817e0a949
Revises: 3ded48d45d42
Create Date: 2023-02-22 13:37:18.798808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '352817e0a949'
down_revision = '3ded48d45d42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
