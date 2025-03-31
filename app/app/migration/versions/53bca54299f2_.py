"""empty message

Revision ID: 53bca54299f2
Revises: 
Create Date: 2025-03-24 03:22:22.375238

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53bca54299f2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
