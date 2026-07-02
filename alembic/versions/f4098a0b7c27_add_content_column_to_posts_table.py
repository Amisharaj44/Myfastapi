"""add content column to posts table

Revision ID: f4098a0b7c27
Revises: ff54a244e5b2
Create Date: 2026-07-01 11:40:44.078927

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4098a0b7c27'
down_revision: Union[str, Sequence[str], None] = 'ff54a244e5b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))


def downgrade():
    op.drop_column('posts','content')
