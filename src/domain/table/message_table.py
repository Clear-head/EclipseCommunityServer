from sqlalchemy import MetaData, Column, String, DateTime, Table, ForeignKey, Text

meta = MetaData()

message_table = Table(
    'message',
    meta,
    Column('id', String(255), primary_key=True),
    Column('receiver', String(255), ForeignKey('users.id'), nullable=False),
    Column('sender', String(255), ForeignKey('users.id'), nullable=False),
    Column('send_at', DateTime, nullable=False),
    Column("body", Text, nullable=True)
)