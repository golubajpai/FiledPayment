"""empty message

Revision ID: 01c1135ee318
Revises: 
Create Date: 2021-01-21 13:11:51.009720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c1135ee318'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credit_card_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('credit_card_number', sa.String(), nullable=True),
    sa.Column('card_holder', sa.String(), nullable=True),
    sa.Column('expiration_date', sa.Date(), nullable=True),
    sa.Column('security_code', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_id', sa.Integer(), nullable=True),
    sa.Column('gateway_used', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['credit_card_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('credit_card_details')
    # ### end Alembic commands ###