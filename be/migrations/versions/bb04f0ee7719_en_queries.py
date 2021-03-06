"""en-queries

Revision ID: bb04f0ee7719
Revises: 9641f472782d
Create Date: 2022-04-25 15:43:40.262945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb04f0ee7719'
down_revision = '9641f472782d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('title_en', sa.String(length=500), nullable=True))
    op.add_column('job', sa.Column('description_en', sa.String(length=10000), nullable=True))
    op.add_column('job', sa.Column('category_en', sa.String(length=250), nullable=True))
    op.add_column('job', sa.Column('requirement_en', sa.String(length=10000), nullable=True))
    op.add_column('job', sa.Column('company_name_en', sa.String(length=500), nullable=True))
    op.add_column('job', sa.Column('company_description_en', sa.String(length=10000), nullable=True))
    op.add_column('job', sa.Column('location_en', sa.String(length=500), nullable=True))
    op.add_column('job', sa.Column('salary_en', sa.String(length=250), nullable=True))
    op.add_column('job', sa.Column('language_en', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'language_en')
    op.drop_column('job', 'salary_en')
    op.drop_column('job', 'location_en')
    op.drop_column('job', 'company_description_en')
    op.drop_column('job', 'company_name_en')
    op.drop_column('job', 'requirement_en')
    op.drop_column('job', 'category_en')
    op.drop_column('job', 'description_en')
    op.drop_column('job', 'title_en')
    # ### end Alembic commands ###
