from sqlalchemy import MetaData, Column, String, DateTime, Table, ForeignKey, Text, Integer

meta = MetaData()

comment_table = Table(
    'comment',
    meta,
    Column('id', String(255), primary_key=True),
    Column('post_id', String(255), ForeignKey("posts.id")),
    Column('user_id', String(255), ForeignKey('users.id')),
    Column('create_at', DateTime, nullable=False),
    Column("body", Text, nullable=True)
)