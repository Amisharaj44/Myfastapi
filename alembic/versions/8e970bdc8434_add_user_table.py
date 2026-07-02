"""add user table

Revision ID: 8e970bdc8434
Revises: f4098a0b7c27
Create Date: 2026-07-01 12:29:28.546485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e970bdc8434'
down_revision: Union[str, Sequence[str], None] = 'f4098a0b7c27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False), 
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
   



def downgrade() -> None:
    op.drop_table('users')
    pass
