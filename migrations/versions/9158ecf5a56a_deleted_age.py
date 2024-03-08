"""Deleted age

Revision ID: 9158ecf5a56a
Revises: 0ae107e784bf
Create Date: 2024-03-08 22:12:53.015389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9158ecf5a56a'
down_revision: Union[str, None] = '0ae107e784bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
