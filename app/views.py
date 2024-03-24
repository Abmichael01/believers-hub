from django.shortcuts import render
from . models import Word


def index(request):
    word = Word.objects.latest("created_at")
    print(word)

    return render(request, "app/index.html", {
        "word": word,
    })

