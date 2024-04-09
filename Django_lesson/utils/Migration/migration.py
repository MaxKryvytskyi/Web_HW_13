# Міграція з mongoDB в posgresql

import sys

sys.path.append("E:\Git_Files\__Python_GOIT__\__Web_2_0__\Web_HW_10\hw_project")

import os 
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author # posgresql

from utils.Load_mongoDB.connect_db import connect # mongoDB
from utils.Load_mongoDB.models import Authors, Quotes # mongoDB

print("start")


authors = Authors.objects()

for author in authors:
    Author.objects.get_or_create(
            fullname = author.fullname,
            born_date = author.born_date,
            born_location = author.born_location,
            description = author.description)
            

quotes = Quotes.objects()

for quote in quotes:
    tags = []
    for tag in quote.tags:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote.quote)))
    if not exist_quote:
        author = Authors.objects.filter(id=quote.author.id).first()
        a = Author.objects.get(fullname=author.fullname)
        q = Quote.objects.create(
            quote=quote.quote,
            goodreads_page = quote.goodreads_page,
            author=a
        )
        for tag in tags:
            q.tags.add(tag)

print("stop")

# py utils\Migration\migration.py migration.py