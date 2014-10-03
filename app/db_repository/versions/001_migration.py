from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alembic_version = Table('alembic_version', pre_meta,
    Column('version_num', VARCHAR(length=32), nullable=False),
)

picture = Table('picture', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('url', VARCHAR),
    Column('description', VARCHAR),
    Column('title', VARCHAR),
)

pictures = Table('pictures', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', TEXT),
    Column('url', TEXT),
    Column('description', TEXT),
)

post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', TIMESTAMP),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=15)),
    Column('password', VARCHAR(length=15)),
    Column('email', VARCHAR(length=120)),
    Column('role', SMALLINT),
)

video = Table('video', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('url', VARCHAR),
    Column('description', VARCHAR),
    Column('title', VARCHAR),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alembic_version'].drop()
    pre_meta.tables['picture'].drop()
    pre_meta.tables['pictures'].drop()
    pre_meta.tables['post'].drop()
    pre_meta.tables['user'].drop()
    pre_meta.tables['video'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alembic_version'].create()
    pre_meta.tables['picture'].create()
    pre_meta.tables['pictures'].create()
    pre_meta.tables['post'].create()
    pre_meta.tables['user'].create()
    pre_meta.tables['video'].create()
