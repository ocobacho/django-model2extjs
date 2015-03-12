import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType

from .models import get_file_for_extjscode, generate_js_foreach_model, generate_modeljs, generate_gridjs, generate_formjs

	
def index(request):  
	return render(request, 'model2extjs/page.html')


def download_model_file(request, appname, module, model):
	jsfile = get_file_for_extjscode(model, module, 'model', appname)
	return HttpResponse( jsfile, content_type = 'application/js')


def download_form_file(request, appname, module, model):
	jsfile = get_file_for_extjscode(model, module, 'form', appname)
	return HttpResponse( jsfile, content_type = 'application/js')


def download_grid_file(request, appname, module, model):
	jsfile = get_file_for_extjscode(model, module, 'grid', appname)
	return HttpResponse( jsfile, content_type = 'application/js')


def list_models(request):
	if request.GET['appname']:
		start = request.GET['start']
		limit = request.GET['limit']
		appname = request.GET['appname']
		modelname = request.GET['model_name'] 
		data = generate_js_foreach_model(appname, modelname, start, limit)
	return HttpResponse(json.dumps(data), content_type = 'application/json')


