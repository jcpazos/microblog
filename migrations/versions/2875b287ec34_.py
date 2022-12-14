"""empty message

Revision ID: 2875b287ec34
Revises: 
Create Date: 2022-09-22 19:08:46.558263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2875b287ec34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('miestudiante')
    op.drop_index('ix_new_user_email', table_name='new_user')
    op.drop_index('ix_new_user_username', table_name='new_user')
    op.drop_table('new_user')
    op.drop_table('py_tbl')
    op.drop_table('student')
    op.drop_table('class')
    op.alter_column('review', 'rating',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=2),
               existing_nullable=True)
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=128),
               nullable=True)
    op.drop_constraint('uniqueName', 'user', type_='unique')
    op.drop_constraint('uniquePassword', 'user', type_='unique')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_unique_constraint('uniquePassword', 'user', ['password'])
    op.create_unique_constraint('uniqueName', 'user', ['username'])
    op.alter_column('user', 'password',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.drop_column('user', 'age')
    op.alter_column('review', 'rating',
               existing_type=sa.String(length=2),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.create_table('class',
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('code', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('room', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='class_pkey')
    )
    op.create_table('student',
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('classId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['classId'], ['class.id'], name='class_fkey'),
    sa.PrimaryKeyConstraint('id', name='student_pkey')
    )
    op.create_table('py_tbl',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('str_col', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('int_col', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='py_tbl_pkey')
    )
    op.create_table('new_user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='new_user_pkey')
    )
    op.create_index('ix_new_user_username', 'new_user', ['username'], unique=False)
    op.create_index('ix_new_user_email', 'new_user', ['email'], unique=False)
    op.create_table('miestudiante',
    sa.Column('codigo', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('edad', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('codigo', name='miestudiante_pkey')
    )
    # ### end Alembic commands ###
