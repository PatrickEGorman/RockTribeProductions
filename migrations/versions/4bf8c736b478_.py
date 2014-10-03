"""empty message

Revision ID: 4bf8c736b478
Revises: None
Create Date: 2014-09-25 16:05:27.305206

"""

# revision identifiers, used by Alembic.
revision = '4bf8c736b478'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('picture')
    op.drop_table('pictures')
    op.drop_table('video')
    op.drop_table('user')
    op.drop_table('migrate_version')
    op.drop_table('post')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), server_default="nextval('post_id_seq'::regclass)", nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], name=u'post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'post_pkey')
    )
    op.create_table('migrate_version',
    sa.Column('repository_id', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('repository_path', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('repository_id', name=u'migrate_version_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default="nextval('user_id_seq'::regclass)", nullable=False),
    sa.Column('username', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('role', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_pkey')
    )
    op.create_table('video',
    sa.Column('id', sa.INTEGER(), server_default="nextval('video_id_seq'::regclass)", nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'video_pkey')
    )
    op.create_table('pictures',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('url', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'pictures_pkey')
    )
    op.create_table('picture',
    sa.Column('id', sa.INTEGER(), server_default="nextval('picture_id_seq'::regclass)", nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'picture_pkey')
    )
    ### end Alembic commands ###
