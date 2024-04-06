from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {'allow_inheritance': True}

class Quotes(Document):
    tags = ListField(StringField(max_length=40))
    author = ReferenceField(Authors, reverse_delete_rule="CASCADE")
    quote = StringField()
    goodreads_page = StringField()