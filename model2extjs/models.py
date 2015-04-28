from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.


def generate_js_foreach_model(appname, model_name, start, limit):
    models = list()
    finish = int(start) + int(limit)
    queryset = get_models(model_name)
    total = queryset.count()
    for ct in queryset[start:finish]:
        m = ct.model_class()
        try:
            if m.__module__:
                models.append({
                    'id': m.__module__ + '.' + m.__name__,
                    'name': m.__name__,
                    'model': generate_modeljs(appname, m),
                    'grid': generate_gridjs(appname, m),
                    'form': generate_formjs(appname, m),
                    'modellink': "files/model/{}/{}/{}.js".format(appname, ct.app_label, m.__name__),
                    'formlink': "files/form/{}/{}/{}form.js".format(appname, ct.app_label, m.__name__),
                    'gridlink': "files/grid/{}/{}/{}/list.js".format(appname, ct.app_label, m.__name__),
                    'applink': "mvc/{}/{}/{}".format(appname, ct.app_label, m.__name__),
                })
        except:
            pass
    return {'data': models, 'total': total}

# get all models filter by model name


def get_models(model_name):
    if model_name == "":
        queryset = ContentType.objects.all()
    else:
        queryset = ContentType.objects.filter(name__contains=model_name)
    return queryset


def generate_formjs(appname, model):
    modelname = model.__name__
    br = "\n"
    code = "Ext.define('" + appname + ".view." + \
        modelname + "." + modelname + "form', {" + br
    code += "    extend: 'Ext.window.Window'," + br
    code += "    alias: 'widget." + modelname + "form'," + br
    code += "    title: '" + modelname.upper() + "'," + br
    code += "    autoShow: true," + br
    code += "    initComponent: function() {" + br
    code += "        this.items = [{" + br
    code += "            xtype: 'form'," + br
    code += "            bodyStyle: 'padding: 10px;'," + br
    code += "            items:[" + br
    code += "            " + get_form_fields(model) + br
    code += "            ]" + br
    code += "        }];" + br
    code += "        this.callParent(arguments);" + br
    code += "    }" + br
    code += "});"
    return code


def generate_controllerjs(appname, model):
    modelname = model.__name__
    br = "\n"
    code = "Ext.define('" + appname + ".controller." + modelname + "', {" + br
    code += "    extend: 'Ext.app.Controller'," + br
    code += "    stores: ['" + modelname + "s']," + br
    code += "    models: ['" + modelname + "']," + br
    code += "    views: ['" + modelname + ".grid', '" + \
        modelname + "." + modelname + "form']," + br
    code += "    init: function() {" + br
    code += "        this.control({" + br
    code += "            '" + modelname + "grid button[action=add]':{" + br
    code += "                click: this.additem," + br
    code += "            }," + br
    code += "        });" + br
    code += "    }," + br
    code += "    additem: function(button){" + br
    code += "       Ext.widget('" + modelname + "form');" + br
    code += "    }," + br
    code += "});"
    return code


def generate_storejs(appname, model):
    modelname = model.__name__
    br = "\n"
    code = "Ext.define('" + appname + ".store." + modelname + "s', {" + br
    code += "    extend: 'Ext.data.Store'," + br
    code += "    model: '" + appname + ".model." + modelname + "'," + br
    code += "    autoLoad: true," + br
    code += "    pageSize: 18," + br
    code += "    proxy: {" + br
    code += "        type: 'rest'," + br
    code += "        url: '...change...'," + br
    code += "        reader: {" + br
    code += "            type: 'json'," + br
    code += "            root: 'results'," + br
    code += "            totalProperty: 'count'," + br
    code += "        }," + br
    code += "        actionMethods: {" + br
    code += "            read: 'GET'," + br
    code += "            create: 'POST'," + br
    code += "            destroy: 'DELETE'," + br
    code += "            update: 'PUT'," + br
    code += "        }" + br
    code += "    }" + br
    code += "});"
    return code


def get_form_fields(model):
    fields = ""
    for f in model._meta.fields:
        if "id" != f.name:
            fields += "{xtype: 'textfield', name: '" + \
                f.name + "', fieldLabel: '" + f.name + "' },"
    return fields


def get_models_fields(model):
    fields = ""
    for f in model._meta.fields:
        fields += "'" + f.name + "', "
    return fields


def generate_modeljs(appname, model):
    modelname = model.__name__
    fields = get_models_fields(model)
    br = '\n'
    code = "Ext.define('" + appname + ".model." + modelname + "', {" + br
    code += "    extend: 'Ext.data.Model'," + br
    code += "    idProperty: 'id'," + br
    code += "    fields: [" + fields + "]" + br
    code += "});" + br

    return code


def generate_gridjs(appname, model):
    modelname = model.__name__
    columns = get_grid_colums(model)
    br = '\n'
    code = "Ext.define('" + appname + ".view." + modelname + ".grid', {" + br
    code += "    extend: 'Ext.grid.Panel'," + br
    code += "    alias: 'widget." + modelname + "grid'," + br
    code += "    title: '" + modelname.upper() + "'," + br
    code += "    store: '" + modelname + "s'," + br
    code += "    initComponent: function() {" + br
    code += "        this.columns = [" + br
    code += "            " + columns + br
    code += "        ];" + br
    code += "        this.callParent(arguments);" + br
    code += "    }," + br
    code += "    dockedItems: [{" + br
    code += "        xtype: 'pagingtoolbar'," + br
    code += "        store: '"+modelname+"s'," + br   
    code += "        dock: 'bottom'," + br 
    code += "    }, {" + br
    code += "        xtype: 'toolbar'," + br
    code += "        store: '"+modelname+"s'," + br   
    code += "        dock: 'top'," + br
    code += "        displayInfo: true," + br
    code += "        items: [{" + br
    code += "            text: 'Insertar'," + br
    code += "            action: 'add'" + br
    code += "        }, {" + br 
    code += "            text: 'Borrar',"  + br
    code += "            action: 'delete'," + br
    code += "        },{" + br
    code += "            text: 'Editar'," + br
    code += "            action: 'edit'" + br
    code += "        }]" + br
    code += "    }]" + br
    code += "});"

    return code


def get_grid_colums(model):
    br = "\n\t    "
    columns = ""
    for f in model._meta.fields:
        columns += "{header: '" + f.name + \
            "', dataIndex: '" + f.name + "',  flex: 1}," + br
    return columns


def get_file_for_extjscode(model, module, component, appname):
    option = get_files_for_extjsmvc(model, module, appname)
    return option[component]


def get_files_for_extjsmvc(model, module, appname):
    model_name = model.lower()
    djmodel = ContentType.objects.get(model=model_name, app_label=module)
    model_class = djmodel.model_class()
    option = {'grid': generate_gridjs(appname, model_class),
              'form': generate_formjs(appname, model_class),
              'model': generate_modeljs(appname, model_class),
              'controller': generate_controllerjs(appname, model_class),
              'store': generate_storejs(appname, model_class)}
    return option
