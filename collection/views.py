from django.shortcuts import render

from collection.models import Thing


def index(request):
    """
    Index page view
    """
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })


def thing_detail(request, slug):
    """
    Thing view
    """
    thing = Thing.objects.get(slug=slug)
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })
