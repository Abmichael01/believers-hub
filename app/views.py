from django.shortcuts import render
from . models import Word, Visit
from datetime import date


def index(request):
    try:
        word = Word.objects.latest("created_at")
    except Word.DoesNotExist:
        word = None

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

def admin_dashboard(request):
    today = date.today()
    todays_visit = Visit.objects.get(date=today)
    return render(request, "app/admin-dashboard.html", {
        "todays_visit": todays_visit,
    })
