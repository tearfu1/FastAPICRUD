"""add column photo

Revision ID: 6b804d349ed6
Revises: 157943cf6c84
Create Date: 2024-08-15 09:14:03.990071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b804d349ed6'
down_revision: Union[str, None] = '157943cf6c84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('photo', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'photo')
    # ### end Alembic commands ###
