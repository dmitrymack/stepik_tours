from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def main_view(request):
    return render(request, 'tours/index.html')


def dep_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request, id):
    return render(request, 'tours/tour.html')


def custom404(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404:</h1><h2>Данной страницы не существует</h2>')


def custom500(request):
    return HttpResponseServerError('<h1>Ошибка 500:</h1><h2>К сожалению, наш сервер сломался</h2>')
