from django.shortcuts import render
from . models import Word, Visit


def index(request):
    word = Word.objects.latest("created_at")

    # visited = request.session.get("visited", None)

    # if visited is None:
    #     visit = Visits.objects.
    #     request.session["visited"] = True
    
    # request.session["visited"] = True

    visit = Visit.objects.first()

    visit.count += 1

    visit.save()


    return render(request, "app/index.html", {
        "word": word,
    })

