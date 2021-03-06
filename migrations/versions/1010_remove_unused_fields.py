"""Remove unused fields

Revision ID: 1010
Revises: 1000
Create Date: 2017-10-04 15:14:48.532073

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '1010'
down_revision = '1000'


def upgrade():
    op.drop_column('contact_information', 'address2')
    op.drop_column('contact_information', 'country')
    op.drop_column('contact_information', 'website')
    op.drop_column('suppliers', 'clients')
    op.drop_column('suppliers', 'esourcing_id')


def downgrade():
    op.add_column('suppliers', sa.Column('esourcing_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('suppliers', sa.Column('clients', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('contact_information', sa.Column('website', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('contact_information', sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('contact_information', sa.Column('address2', sa.VARCHAR(), autoincrement=False, nullable=True))
