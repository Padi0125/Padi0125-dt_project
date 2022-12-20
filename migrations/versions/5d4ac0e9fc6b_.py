"""empty message

Revision ID: 5d4ac0e9fc6b
Revises: 89f2f85474c4
Create Date: 2022-12-03 10:10:04.789044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d4ac0e9fc6b'
down_revision = '89f2f85474c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_constraint('uq_item_my_user', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_item_my_user', ['my_user'])

    # ### end Alembic commands ###
