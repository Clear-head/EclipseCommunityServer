from sqlalchemy import MetaData, Column, String, DateTime, Table, ForeignKey, Text, Integer

meta = MetaData()

message_table = Table(
    'message',
    meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('receiver', String(255), ForeignKey('users.id'), nullable=False),
    Column('sender', String(255), ForeignKey('users.id'), nullable=False),
    Column('send_at', DateTime, nullable=False),
    Column("body", Text, nullable=True)
)