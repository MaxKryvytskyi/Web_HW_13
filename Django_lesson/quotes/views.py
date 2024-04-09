from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from quotes.models import Tag, Quote, Author
from .forms import AuthorForm, QuoteForm, TagForm


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author(request, author_id):
    author_info = Author.objects.get(id=author_id)
    return render(request, "quotes/author.html", context={"author": author_info})


def tag_search(request, tag):
    # select qt.name, qqt.quote_id 
    # from public.quotes_tag qt 
    # join public.quotes_quote_tags qqt on qqt.tag_id = qt.id 
    # join public.quotes_quote qq on qq.id = qqt.quote_id 
    # WHERE qt.name = 'love';

    # --Запрос на поиск цитат за тегом
    tags_search = tag
    quotes_id = Tag.objects.filter(name=tag).values('name', 'quote__id')
    quotes = []
    for item in quotes_id:
        quote = Quote.objects.get(id=item['quote__id'])
        data = Quote.tags.through.objects.filter(quote_id=quote.id).values('tag_id')
        tags = []
        for tag_id in data:
            tag_name = Tag.objects.filter(id=tag_id["tag_id"]).values('name')
            tag_name = list(tag_name.values_list('name', flat=True))
            tags.append(*tag_name)

        quotes.append({"id" : quote.id,
                       "quote" : quote.quote,
                       "tags" : tags,
                       "author" : { "fullname" : quote.author.fullname, "id" : quote.author.id},
                       "goodreads_page" : quote.goodreads_page})  
    return render(request, "quotes/tag_search.html", context={"quotes": quotes, "tags_search": tags_search})


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes\create_author.html", {'form' : form})
        
    return render(request, "quotes\create_author.html", {'form' : AuthorForm})


def create_quote(request):
    tagss = Tag.objects.all().order_by('name')

    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['author'])
            print(form.cleaned_data['quote'])
            print(form.cleaned_data['tags'])
            print(form.cleaned_data['goodreads_page'])
            form.save()
            return redirect(to="quotes:root")
        else:

            return render(request, "quotes\create_quote.html", {'form' : form, "tagss" : tagss})
        
    return render(request, "quotes\create_quote.html", {'form' : QuoteForm, "tagss" : tagss})


def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes\create_tag.html", {'form' : form})
        
    return render(request, "quotes\create_tag.html", {'form' : TagForm})