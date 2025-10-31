from sqlalchemy import MetaData, Column, String, DateTime, Table, ForeignKey, Text, Integer

meta = MetaData()

posts_table = Table(
    'posts',
    meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    Column('user_id', String(255), ForeignKey('users.id'), nullable=False),
    Column('create_at', DateTime, nullable=False),
    Column("body", Text, nullable=True)
)