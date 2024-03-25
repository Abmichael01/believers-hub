from django.shortcuts import render
from . models import Word, Visit
from datetime import date


def index(request):
    word = Word.objects.latest("created_at")

    # visited = request.session.get("visited", None)

    # if visited is None:
    #     visit = Visits.objects.
    #     request.session["visited"] = True
    
    # request.session["visited"] = True
    today = date.today()

    visit, created = Visit.objects.get_or_create(date=today)

    visit.count += 1

    visit.save()


    return render(request, "app/index.html", {
        "word": word,
    })

