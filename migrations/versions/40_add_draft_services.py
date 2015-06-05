"""empty message

Revision ID: 37ac005a48c3
Revises: 20_adding_json_index_to_services
Create Date: 2015-06-02 18:32:08.399213

"""

# revision identifiers, used by Alembic.
revision = '40_add_draft_services'
down_revision = '20_adding_json_index_to_services'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('draft_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.String(), nullable=False),
    sa.Column('supplier_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.String(), nullable=False),
    sa.Column('updated_reason', sa.String(), nullable=False),
    sa.Column('data', postgresql.JSON(), nullable=True),
    sa.Column('framework_id', sa.BigInteger(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['framework_id'], ['frameworks.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.supplier_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_draft_services_framework_id'), 'draft_services', ['framework_id'], unique=False)
    op.create_index(op.f('ix_draft_services_service_id'), 'draft_services', ['service_id'], unique=True)
    op.create_index(op.f('ix_draft_services_supplier_id'), 'draft_services', ['supplier_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_draft_services_supplier_id'), table_name='draft_services')
    op.drop_index(op.f('ix_draft_services_service_id'), table_name='draft_services')
    op.drop_index(op.f('ix_draft_services_framework_id'), table_name='draft_services')
    op.drop_table('draft_services')
    ### end Alembic commands ###
