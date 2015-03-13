==================
Django-model2extjs
==================

Model2extjs is a simple Django app for generating Extjs code (grids, forms and models) from Django models.

***********
Description
***********

Sometimes if We are working with Django and Extjs we may have to write the same model fields in many places of our Extjs app and that can get very annoying. Django-model2extjs tries to achieve a simple solution to that problem by using the models in our django project to generate the code for different Extjs components(grids, forms and models). The code generated can be further extended to fit the needs of each application. 

- Django-model2extjs doesn't add any database table to your project.
- The code generated uses Extjs MVC

Detailed documentation is in the "docs" directory.

***********
Quick start 
***********

1. Download the zip file from https://github.com/ocobacho/django-model2extjs/archive/master.zip

2. Go to the directoy where you download it and do a pip install like this
	"pip install --user django-model2extjs.zip"
	
	or just copy the folder "model2extjs" to your django project directory.
	
3. Add "model2extjs" to "INSTALLED_APPS" in your project settings
	INSTALLED_APPS = (
        ...
        'model2extjs',
    )
4. include the "model2extjs.urls" to your project urls file
	...
	url(r'^model2extjs/', include('model2extjs.urls'))
	
5. Visit the included url "http://127.0.0.1:8000/model2extjs"

************************
A brief Markdown Example
************************

1. Visit the included url "http://127.0.0.1:8000/model2extjs"
2. Enter your Extjs app name 
3. Click load models (The list of models from your django project should appear)
4. Download generated files from the list
or
4. Double click on the models for selecting and copying the code 
