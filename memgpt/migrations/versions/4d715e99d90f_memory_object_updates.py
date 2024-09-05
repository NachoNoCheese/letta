"""memory object updates

Revision ID: 4d715e99d90f
Revises: 0f88ad62279d
Create Date: 2024-09-04 21:20:36.653422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d715e99d90f'
down_revision: Union[str, None] = '0f88ad62279d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('block', '_organization_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.add_column('passage', sa.Column('user_id', sa.String(), nullable=True))
    op.add_column('passage', sa.Column('_agent_id', sa.UUID(), nullable=False))
    op.alter_column('passage', '_document_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'passage', 'agent', ['_agent_id'], ['_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'passage', type_='foreignkey')
    op.alter_column('passage', '_document_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_column('passage', '_agent_id')
    op.drop_column('passage', 'user_id')
    op.alter_column('block', '_organization_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###
