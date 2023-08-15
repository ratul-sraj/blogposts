from typing import List, Dict

from django.shortcuts import render

posts: list[dict[str, str] | dict[str, str]] = [
    {
        "author": "ratul",
        "title": "First post",
        "content": "Donec venenatis lacus id hendrerit hendrerit. Suspendisse potenti. "
                   "Maecenas ut mollis libero. Quisque ac nisl sodales, mollis urna sit amet, "
                   "aliquam nisl. Nunc sit amet elit eu magna vulputate facilisis. Donec faucibus malesuada elit et bibendum. "
                   "Fusce blandit ante vehicula aliquet tempor. Nulla facilisi. Morbi mollis laoreet felis ut interdum. Sed tristique "
                   "felis cursus varius egestas. Nulla volutpat porta est, at imperdiet ante condimentum sed. Integer interdum arcu "
                   "erat, non rhoncus nunc cursus a. Sed feugiat luctus erat at finibus. Vestibulum at ex mollis, "
                   "laoreet justo sit amet, scelerisque mauris. Vestibulum molestie ac justo eget dictum. Nullam fermentum ac "
                   "mi quis posuere.",
        "date_posted": "Aug 27 2018"

    }, {
        "author": "Jane",
        "title": "Second post",
        "content": "Donec venenatis lacus id hendrerit hendrerit. Suspendisse potenti. "
                   "Maecenas ut mollis libero. Quisque ac nisl sodales, mollis urna sit amet, "
                   "aliquam nisl. Nunc sit amet elit eu magna vulputate facilisis. Donec faucibus malesuada elit et bibendum. "
                   "Fusce blandit ante vehicula aliquet tempor. Nulla facilisi. Morbi mollis laoreet felis ut interdum. Sed tristique "
                   "felis cursus varius egestas. Nulla volutpat porta est, at imperdiet ante condimentum sed. Integer interdum arcu "
                   "erat, non rhoncus nunc cursus a. Sed feugiat luctus erat at finibus. Vestibulum at ex mollis, "
                   "laoreet justo sit amet, scelerisque mauris. Vestibulum molestie ac justo eget dictum. Nullam fermentum ac "
                   "mi quis posuere.",
        "date_posted": "Aug 28 2018"
    }
]


# Create your views here.

def home(req):
    context = {"posts": posts}
    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, "blog/about.html",{"title": "About"})
