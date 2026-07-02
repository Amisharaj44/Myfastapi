"""create posts table

Revision ID: ff54a244e5b2
Revises: ccb8791c859d
Create Date: 2026-06-30 19:14:25.605275

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff54a244e5b2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,
                                     primary_key=True),sa.Column('title',sa.String(),nullable=False))
    
    


def downgrade():
    op.drop_table('posts')
    pass
