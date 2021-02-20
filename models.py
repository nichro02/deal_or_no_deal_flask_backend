from peewee import *
from flask_login import UserMixin

import datetime

#link to database
DATABASE = PostgresqlDatabase('deal_or_no_deal', host='localhost', port=5432)

#instantiate models
#instantiate base model that specifies database and can be used for subsequent models
class BaseModel(Model):
    class Meta:
        database = DATABASE

#Player Model
class Player(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')

#Game Model
class Game(BaseModel):
    user_id = ForeignKeyField(Player)
    score = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now)

#Comment Model
#self-referential foreign keys: http://docs.peewee-orm.com/en/latest/peewee/models.html#self-referential-foreign-keys
class Comment(BaseModel):
    user_id = ForeignKeyField(Player)
    body = CharField()
    is_reply = BooleanField(default=False)
    parent_id = ForeignKeyField('self', backref='children', null=True)

#initialize database -> connect, create_tables, close_tables
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Player, Game, Comment], safe=True)
    print('Tables created')
    DATABASE.close()