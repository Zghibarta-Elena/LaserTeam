"""Initial migration from SQL schema

Revision ID: 9200dc26ff81
Revises: 0d3dc62babce
Create Date: 2024-11-03 20:38:54.839245

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9200dc26ff81'
down_revision: Union[str, None] = '0d3dc62babce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Examen',
    sa.Column('id_Examen', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_Profesor', sa.Integer(), nullable=False),
    sa.Column('id_Cerere', sa.Integer(), nullable=False),
    sa.Column('id_Materie', sa.Integer(), nullable=False),
    sa.Column('ora', sa.Time(), nullable=False),
    sa.Column('sala', sa.VARCHAR(length=20), nullable=False),
    sa.ForeignKeyConstraint(['id_Cerere'], ['Cerere.id_Cerere'], ),
    sa.ForeignKeyConstraint(['id_Materie'], ['Materie.id_Materie'], ),
    sa.ForeignKeyConstraint(['id_Profesor'], ['Profesor.id_Profesor'], ),
    sa.PrimaryKeyConstraint('id_Examen')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Examen')
    # ### end Alembic commands ###
