import os
import shutil

from django.test import TestCase
from django.core.urlresolvers import reverse

from django.contrib.contenttypes.models import ContentType

from .myos import (
    generate_store_file, generate_form_file,
    generate_grid_file, generate_model_file,
    compress_folder, makedir, changedir,
    generate_mvc_structure, generate_controller_file)
from .models import (
    generate_controllerjs, generate_storejs, get_file_for_extjscode)
# Create your tests here.


class ExtMvcTestCase(TestCase):
    # views test

    def setUp(self):
        self.staticdir = os.path.join(os.path.dirname(__file__), "static")
        self.mvc = "extjsmvc"
        self.path = os.path.join(self.staticdir, "model2extjs")
        self.current = os.path.join(self.path, "testfolder")
        if os.access(self.current, os.F_OK):
            os.chdir(self.current)
        else:
            os.mkdir(self.current)
            os.chdir(self.current)

    def test_genarate_mvc_view(self):
        data = self.get_params_for_mvc()
        self.assertEqual(data["response"].status_code, 302)
        currentdir = os.getcwd()
        os.chdir(self.path)
        self.assertTrue(os.access("app.tar", os.F_OK))
        os.chdir(currentdir)

    def test_genarate_model_file_view(self):
        data = self.get_params_for_mvc()
        self.assertEqual(data["response"].status_code, 302)
        self.assertTrue(os.access("model", os.F_OK))
        self.assertTrue(os.access("model/" + data["model"] + ".js", os.F_OK))

    def test_genarate_grid_file_view(self):
        data = self.get_params_for_mvc()
        self.assertEqual(data["response"].status_code, 302)
        self.assertTrue(os.access("view", os.F_OK))
        self.assertTrue(
            os.access("view/" + data["model"] + "/grid.js", os.F_OK))

    def test_generate_store_file_view(self):
        data = self.get_params_for_mvc()
        self.assertEqual(data["response"].status_code, 302)
        self.assertTrue(os.access("store", os.F_OK))
        self.assertTrue(
            os.access("store/" + data["model"] + "s.js", os.F_OK))

    def get_params_for_mvc(self):
        contenttype = ContentType.objects.all()[0]
        model = contenttype.name
        extjsapp = "Appname"
        app_label = contenttype.app_label
        url = reverse('mvc', args=[extjsapp, app_label, model])
        response = self.client.get(url)

        data = {"response": response,
                "model": model}
        os.chdir(self.path)
        os.chdir(self.mvc)
        return data

    def test_genarate_form_file_view(self):
        data = self.get_params_for_mvc()
        self.assertEqual(data["response"].status_code, 302)
        self.assertTrue(os.access("view", os.F_OK))
        self.assertTrue(
            os.access("view/" +
                      data["model"] + "/" +
                      data["model"] + "form.js",
                      os.F_OK))

    def change_dir_for_test(self):
        os.chdir(self.path)
        os.chdir(self.mvc)

    def test_make_controller_file(self):
        filecontent = "filecontrollercontent"
        filetest = "filecontrolertest"
        self.change_dir_for_test()
        generate_controller_file(filecontent, filetest)
        os.chdir("controller")
        self.assertTrue(os.access(filetest + ".js", os.F_OK))
        content = ""
        with open(filetest + ".js") as myfile:
            content = myfile.readline()
        self.assertIn(filecontent, content)

    def test_make_form_file(self):
        filecontent = "filecontent"
        filetest = "filetest"
        self.change_dir_for_test()
        generate_form_file(filecontent, filetest)
        os.chdir("view")
        os.chdir(filetest)
        self.assertTrue(os.access(filetest + "form.js", os.F_OK))
        content = ""
        with open(filetest + "form.js") as myfile:
            content = myfile.readline()
        self.assertIn(filecontent, content)

    def test_make_grid_file(self):
        filecontent = "filecontent"
        filetest = "filetest"

        self.change_dir_for_test()
        generate_grid_file(filecontent, filetest)
        os.chdir("view")
        os.chdir(filetest)
        self.assertTrue(os.access("grid.js", os.F_OK))
        content = ""
        with open("grid.js") as myfile:
            content = myfile.readline()
        self.assertIn(filecontent, content)

    def test_make_model_file(self):
        filecontent = "filecontent"
        filetest = "filetest"

        self.change_dir_for_test()
        generate_model_file(filecontent, filetest)
        os.chdir("model")
        self.assertTrue(os.access(filetest + ".js", os.F_OK))
        content = ""
        with open(filetest + ".js") as myfile:
            content = myfile.readline()
        self.assertIn(filecontent, content)

    def test_make_store_file(self):
        filecontent = "filecontent"
        filetest = "filetest"

        self.change_dir_for_test()
        generate_store_file(filecontent, filetest)
        os.chdir("store")
        self.assertTrue(os.access(filetest + "s.js", os.F_OK))
        content = ""
        with open(filetest + "s.js") as myfile:
            content = myfile.readline()
        self.assertIn(filecontent, content)

    def test_store_content(self):
        contenttype = ContentType.objects.all()[0]
        storejs = generate_storejs("myapp", contenttype.model_class())
        self.assertIn(
            "Ext.define('myapp.store." + contenttype.name + "s', {", storejs)

    def test_controller_content(self):
        contenttype = ContentType.objects.all()[0]
        js = generate_controllerjs("myapp", contenttype.model_class())
        self.assertIn(
            "Ext.define('myapp.controller." + contenttype.name + "', {", js)
        self.assertIn(
            contenttype.name + "grid button[action=add]", js)
        self.assertIn(
            "Ext.widget('" + contenttype.name + "form');", js)

    def test_store_with_get_file_for_extjs_code(self):
        contenttype = ContentType.objects.all()[0]
        storejs = get_file_for_extjscode(
            contenttype.name, contenttype.app_label, "store", "myapp")
        self.assertIn(
            "Ext.define('myapp.store." + contenttype.name + "s', {", storejs)

    def test_compress_files(self):
        os.chdir(self.path)
        generate_mvc_structure()
        compress_folder(self.mvc)

        self.assertTrue(os.access("app.tar", os.F_OK))
        os.remove("app.tar")
        self.assertFalse(os.access("app.tar", os.F_OK))

    def test_make_dir(self):
        folder = "makedir"
        makedir(folder)
        self.assertTrue(os.access(folder, os.F_OK))
        os.rmdir(folder)
        self.assertFalse(os.access(folder, os.F_OK))

    def test_change_dir(self):
        folder = "testchangefolder"
        changedir(folder)
        current = os.path.join(self.current, folder)
        self.assertEqual(os.getcwd(), current)
        os.chdir('..')
        self.assertTrue(os.access(folder, os.F_OK))
        os.rmdir(current)
        self.assertFalse(os.access(folder, os.F_OK))

    def test_generate_mvc_structure(self):
        generate_mvc_structure()
        self.assertTrue(os.access("model", os.F_OK))
        self.assertTrue(os.access("controller", os.F_OK))
        self.assertTrue(os.access("store", os.F_OK))
        self.assertTrue(os.access("view", os.F_OK))

    def test_folders_delete(self):
        #self.assertTrue(os.access(self.current, os.F_OK))
        # os.rmdir(self.current)
        os.chdir(self.path)
        self.assertTrue(os.access(self.current, os.F_OK))
        shutil.rmtree(self.current)
        self.assertFalse(os.access(self.current, os.F_OK))
        self.assertTrue(os.access(self.mvc, os.F_OK))
        shutil.rmtree(self.mvc)
        self.assertFalse(os.access(self.mvc, os.F_OK))
