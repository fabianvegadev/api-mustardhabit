"""reiniciando tablas

Revision ID: 56e9752ce01c
Revises: 
Create Date: 2024-10-19 14:49:18.607940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e9752ce01c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('habits',
    sa.Column('habit_id', sa.Integer(), nullable=False),
    sa.Column('habit_name', sa.String(length=100), nullable=False),
    sa.Column('time_of_day', sa.Enum('mañana', 'tarde', 'noche', name='times_of_day_enum'), nullable=True),
    sa.Column('habit_status', sa.Boolean(), nullable=False, server_default=sa.true()),
    sa.PrimaryKeyConstraint('habit_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('user_password', sa.String(length=200), nullable=False),
    sa.Column('user_status', sa.Boolean(), nullable=False, server_default=sa.true()),
    sa.Column('user_created_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('assignments',
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('assignment_status', sa.Boolean(), nullable=False, server_default=sa.true()),
    sa.Column('fk_user_id', sa.Integer(), nullable=False),
    sa.Column('fk_habit_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fk_habit_id'], ['habits.habit_id'], ),
    sa.ForeignKeyConstraint(['fk_user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('assignment_id')
    )
    op.create_table('completed_dates',
    sa.Column('completed_date_id', sa.Integer(), nullable=False),
    sa.Column('completed_date', sa.Date(), nullable=False),
    sa.Column('fk_assignment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fk_assignment_id'], ['assignments.assignment_id'], ),
    sa.PrimaryKeyConstraint('completed_date_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('completed_dates')
    op.drop_table('assignments')
    op.drop_table('users')
    op.drop_table('habits')
    # ### end Alembic commands ###
