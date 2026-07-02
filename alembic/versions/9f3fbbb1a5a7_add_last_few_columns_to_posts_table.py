"""add last few columns to posts table

Revision ID: 9f3fbbb1a5a7
Revises: 40d79bfa23d7
Create Date: 2026-07-01 16:04:02.437061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f3fbbb1a5a7'
down_revision: Union[str, Sequence[str], None] = '40d79bfa23d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
