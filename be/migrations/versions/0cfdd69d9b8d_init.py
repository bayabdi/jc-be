"""INIT

Revision ID: 0cfdd69d9b8d
Revises: 
Create Date: 2022-03-17 12:33:16.118402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cfdd69d9b8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('surname', sa.String(length=250), nullable=True),
    sa.Column('hashed_password', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('category', sa.String(length=250), nullable=True),
    sa.Column('requirement', sa.String(length=1000), nullable=True),
    sa.Column('company_name', sa.String(length=500), nullable=True),
    sa.Column('company_description', sa.String(length=1000), nullable=True),
    sa.Column('location', sa.String(length=500), nullable=True),
    sa.Column('company_size', sa.String(length=500), nullable=True),
    sa.Column('company_logo', sa.String(length=500), nullable=True),
    sa.Column('salary', sa.String(length=250), nullable=True),
    sa.Column('post_date', sa.String(length=250), nullable=True),
    sa.Column('language', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_job_id'), 'job', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_job_id'), table_name='job')
    op.drop_table('job')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
