"""cascade id dosen

Revision ID: 662dbf4480fa
Revises: 10939a3d65c6
Create Date: 2024-03-25 12:49:21.494329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662dbf4480fa'
down_revision = '10939a3d65c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_dua'], ['id'])
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_satu'], ['id'])

    # ### end Alembic commands ###
