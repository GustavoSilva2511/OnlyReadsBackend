"""empty message

Revision ID: 83967228fe21
Revises: 
Create Date: 2025-12-04 10:00:33.530705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83967228fe21'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('email', sa.String(100), unique=True),
        sa.Column('password', sa.String(150))
    )

    op.create_table(
        'enterprises',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cnpj', sa.String(14), unique=True),
        sa.Column('fantasy_name', sa.String(50)),
        sa.Column('cep', sa.String(8)),
        sa.Column('latitude', sa.Float(precision=8)),
        sa.Column('longitude', sa.Float(precision=8))
    )


def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('enterprises')