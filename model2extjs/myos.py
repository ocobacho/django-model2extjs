import os
# from tarfile import TarFile
import tarfile


def makedir(folder):
    if os.access(folder, os.F_OK):
        pass
    else:
        os.mkdir(folder)


def changedir(folder):
    if os.access(folder, os.F_OK):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)


def get_model2exjt_static_dir():
    static = os.path.join(os.path.dirname(__file__), "static")
    mypath = os.path.join(static, "model2extjs")
    return mypath


def generate_mvc_structure():
    changedir(
        os.path.join(
            get_model2exjt_static_dir(), 'extjsmvc'))
    makedir('model')
    makedir('controller')
    makedir('store')
    makedir('view')


def generate_form_file(myfile, modelname):
    os.chdir("view")
    changedir(modelname)
    makefile(myfile, modelname + "form")
    os.chdir("..")


def generate_controller_file(myfile, modelname):
    os.chdir("controller")
    makefile(myfile, modelname)


def generate_model_file(myfile, modelname):
    os.chdir("model")
    makefile(myfile, modelname)


def generate_grid_file(myfile, modelname):
    os.chdir("view")
    changedir(modelname)
    makefile(myfile, "grid")
    os.chdir("..")


def generate_store_file(myfile, modelname):
    os.chdir("store")
    makefile(myfile, modelname + "s")


def makefile(myfile, filename):
    with open(filename + '.js', 'w') as f:
        f.write(myfile)
    os.chdir("..")


def compress_folder(mydir):
    os.chdir(get_model2exjt_static_dir())
    mytar = tarfile.open("app.tar", "w")
    mytar.add(mydir)
    mytar.close()
