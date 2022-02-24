from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
import tours.data as data
from random import randint


def main_view(request):
    copytour = data.tours.copy()
    rnd = []
    rndtour = []
    while len(rnd) != 6:
        a = randint(1, len(data.tours))
        if a not in rnd:
            rnd += [a]
            copytour[a]['numtour'] = a
            rndtour += [copytour[a]]

    return render(request, 'tours/index.html', context={
        "subtitle": data.subtitle,
        "descr": data.description,
        "rndtour": rndtour,
    })


def dep_view(request, departure):
    if departure in data.departures.keys():
        return render(request, 'tours/departure.html')
    else:
        raise Http404


def tour_view(request, id):
    if 1 <= id <= len(data.tours):
        dep = data.departures[data.tours[id]["departure"]]
        return render(request, 'tours/tour.html', context={"id": id, "tour": data.tours[id], "dep": dep})
    else:
        raise Http404


def custom404(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404:</h1><h2>Данной страницы не существует</h2>')


def custom500(request):
    return HttpResponseServerError('<h1>Ошибка 500:</h1><h2>К сожалению, наш сервер сломался</h2>')
