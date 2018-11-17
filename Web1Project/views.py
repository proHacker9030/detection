from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from models import HandleFile
from models import UploadFileForm
from django.core import serializers


def hello(request, d):
    try:
        d = int(d)
        html = "d = %s" % d
        return HttpResponse(html)
    except ValueError:
        raise Http404


def index(request):
    all_methods = Method.objects.all()
    title = 'Main'
    return render(request, 'index.html', {'title': title, 'methods': all_methods})


def method(request, id):
    all_methods = Method.objects.all()
    current = Method.objects.filter(id=id).all()
    title = current.first().name
    return render(request, 'method.html', {'methods': all_methods, 'current_method': id, 'title': title})


@csrf_exempt
def upload_file(request):
    if request.is_ajax() and request.method == 'POST':
        form = UploadFileForm.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = handle_uploaded_file(request.FILES['file'], request.POST.get('method_id'), False)
            serialized_result = serializers.serialize('json', result)
            return HttpResponse(serialized_result)
    else:
        return "Method is allowed only for ajax post requests"


@csrf_exempt
def choose(request):
    if request.is_ajax():
        result = handle_uploaded_file(False, request.POST.get('method_id'), request.POST.get('name'))
        serialized_result = serializers.serialize('json', result)
        return HttpResponse(serialized_result)
    else:
        return "Method is allowed only for ajax post requests"


def handle_uploaded_file(f, method_id, name):
    if name:
        handle_file = HandleFile.HandleFile(name, method_id)
        handle_file.handle()
        # results = Result.objects.filter(method_id=method_id).all()
        results = Result.objects.raw("SELECT * FROM Web1Project_result WHERE date =  (SELECT MAX(date) FROM Web1Project_result)")
        return results
    else:
        with open('C:/Users/Наиль/PycharmProjects/Web1/media/uploaded_images/' + f.name,
                  'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    handle_file = HandleFile.HandleFile(name, method_id)
    handle_file.handle()
    # results = Result.objects.filter(method_id=method_id).all()
    results = Result.objects.raw("SELECT * FROM Web1Project_result WHERE date =  (SELECT MAX(date) FROM Web1Project_result)")
    return results


