import base64
import io
import urllib
import matplotlib.pyplot as plt
from django.shortcuts import render
from applications.graph_generator.utils import graph_gen


# Create your views here.


def home(request):
    generator = graph_gen.call_graph_generator()
    return render(request, 'home.html', {'data': generator})


def graph1_view(request):
    """
    Render graph
    :param request:
    :return: graph
    """
    # TODO: напиши нормально функцию генерации
    # Все темплейты хранятся в общей папке templates, сделай их используя extends шаблонов
    template = ''
    context = {}

    return render(request, template, context)
