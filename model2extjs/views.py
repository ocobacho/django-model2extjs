import json
import os

from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from .models import (get_file_for_extjscode,
                     get_files_for_extjsmvc,
                     generate_js_foreach_model,)
from .myos import (generate_store_file, compress_folder,
                      generate_form_file, generate_controller_file,
                      generate_grid_file,
                      generate_mvc_structure, generate_model_file)


def index(request):
    return render(request, 'model2extjs/page.html')


def generate_mvc(request, appname, module, model):
    generate_mvc_structure()
    files = get_files_for_extjsmvc(model, module, appname)
    generate_form_file(files["form"], model)
    generate_model_file(files["model"], model)
    generate_grid_file(files["grid"], model)
    generate_store_file(files["store"], model)
    generate_controller_file(files["controller"], model)
    compress_folder("extjsmvc")

    return HttpResponseRedirect("/static/model2extjs/app.tar")


def download_model_file(request, appname, module, model):
    jsfile = get_file_for_extjscode(model, module, 'model', appname)
    return HttpResponse(jsfile, content_type='application/js')


def download_store_file(request, appname, module, model):
    jsfile = get_file_for_extjscode(model, module, 'store', appname)
    return HttpResponse(jsfile, content_type='application/js')


def download_form_file(request, appname, module, model):
    jsfile = get_file_for_extjscode(model, module, 'form', appname)
    return HttpResponse(jsfile, content_type='application/js')


def download_grid_file(request, appname, module, model):
    jsfile = get_file_for_extjscode(model, module, 'grid', appname)
    return HttpResponse(jsfile, content_type='application/js')


def download_controller_file(request, appname, module, model):
    jsfile = get_file_for_extjscode(model, module, 'controller', appname)
    return HttpResponse(jsfile, content_type='application/js')


def list_models(request):
    if request.GET['appname']:
        start = request.GET['start']
        limit = request.GET['limit']
        appname = request.GET['appname']
        modelname = request.GET['model_name']
        data = generate_js_foreach_model(appname, modelname, start, limit)
    return HttpResponse(json.dumps(data), content_type='application/json')
