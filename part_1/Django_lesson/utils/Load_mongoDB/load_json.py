import json
from models import Authors, Quotes
from connect_db import connect


def main():
    with open("Json/authors.json", "r+", encoding='utf-8') as file:
        authors_data = json.load(file)

    with open("Json/quotes.json", "r+", encoding='utf-8') as file:
        quotes_data = json.load(file)

    for author_data in authors_data:
        author = Authors(fullname = author_data["fullname"],
                         born_date = author_data["born_date"],
                         born_location = author_data["born_location"],
                         description = author_data["description"])
        author.save()

    for quote_data in quotes_data:
        author_name = quote_data["author"]
        author = Authors.objects(fullname=author_name).first()

        if author:
            quote_data["author"] = author
            quote = Quotes(tags = quote_data["tags"],
                           author = quote_data["author"],
                           quote = quote_data["quote"],
                           goodreads_page = quote_data["goodreads_page"])
            quote.save()
        
# if __name__ == "__main__":
#     main()
#     print("OK")