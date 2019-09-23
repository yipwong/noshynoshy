from django.shortcuts import render
from . models import Page
# from django.http import HttpResponse


def index(request, pagename):
    # return HttpResponse("<h1>The Meandco Homepage</h1>")
    # assert False
    pagename = '/' + pagename
    print("*************")
    print(pagename)
    print("*************")
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)
