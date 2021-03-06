import subprocess
import tempfile
import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

def _exec_notebook(path):
    ''' 
        Execute a jupyter notebook via nbconvert.
    '''
    print("path passed in: ", path)
    print("os.getcwd: ", os.getcwd())
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert",
                "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--ExecutePreprocessor.kernel_name=python3",
                #"--output", fout.name , path]
                "--output", os.getcwd() + "/temp102218" , path]
        print(" ".join(args))
        subprocess.check_call(args)
    return
        
# https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
def _process_notebook(path):
    ''' 
        Execute a jupyter notebook via nbconvert and collect the output.
        
        returns:    parsed nb object
                    execution errors
    '''
    # in_file = '/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb'
    dirname, in_file = os.path.split(path)
    os.chdir(dirname)
    # convert *.ipynb from jupyter notebook to py notebook
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--output", fout.name, path]
        # submodule allows you to spawn new processes, connect to their input/
        # output/error pipes, and obtain their return codes.
        subprocess.check_call(args)
        # seek() sets the file's current position.
        fout.seek(0)
        nb = nbformat.read(os.getcwd() + "/temp031420.ipynb", nbformat.current_nbformat)

    errors = [output for cell in nb.cells if "outputs" in cell
                for output in cell["outputs"]\
                if output.output_type == "AssertionError"]

    for out in nb.cells:
        if out.output_type == 'error':
            raise RuntimeError('Error executing the notebook.')


    try:
        out = ExecutePreprocessor.preprocess(nb, {'metadata': {'path': path}})
    except CellExecutionError:
        out = None
        msg = 'Error executing the notebook "%s".\n\n' % notebook_filename
        msg += 'See notebook "%s" for the traceback.' % notebook_filename_out
        print(msg)
        raise
    finally:
        nb_out = 'JN_execute_out'
        with open(nb_out, mode='wt') as f:
            nbformat.write(nb, f)

    return nb, errors

def test():
    cwd = os.getcwd()
    print(cwd)
    # local
    # notebook_path = cwd + '/TestingAppVeyor/tests/example.ipynb'
    # appveyor
    notebook_path = cwd + '/tests/example.ipynb'
    _exec_notebook(notebook_path)
    # nb, errors = _process_notebook(notebook_path)
    # assert errors == []
    # _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/example.ipynb')
    # _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb') 
    # nb, errors = _process_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb')
    # notebook_path = cwd + 'tests/Orbit_Period_Uncertainty_Trending_demo.ipynb'
    # nb, errors = _process_notebook(notebook_path)
    # assert that errors is empty, otherwise fail
    # assert errors == []

def main():
    test()


if __name__ == "__main__":
    main()
    
    


#import subprocess
#import tempfile
#import nbformat
#import os
#from nbconvert.preprocessors import ExecutePreprocessor
#from nbconvert.preprocessors import CellExecutionError

#def _exec_notebook(path):
#    ''' 
#        Execute a jupyter notebook via nbconvert.
#    '''
#    # print("exec notebookt path passed in: ", path)
#    # print("exec notebook os.getcwd: ", os.getcwd())
#    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
#        args = ["jupyter", "nbconvert",
#                "--to", "notebook", "--execute",
#                "--ExecutePreprocessor.timeout=120",
#                "--ExecutePreprocessor.kernel_name=python3",
#                #"--output", fout.name , path]
#                "--output", os.getcwd() + "/temp031420" , path]
#        print(" ".join(args))
#        subprocess.check_call(args)
#    return
#        
## https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
#def _process_notebook(path):
#    ''' 
#        Execute a jupyter notebook via nbconvert and collect the output.
#        
#        returns:    parsed nb object
#                    execution errors
#    '''
#    # in_file = '/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb'
#    # dirname, in_file = os.path.split(path)
#    # print("process notebookt path passed in: ", path)
#    # print("process notebook os.getcwd: ", os.getcwd())
#    #os.chdir(dirname)
#    # convert *.ipynb from jupyter notebook to py notebook
#    #with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
#    #    args = ["jupyter", "nbconvert",
#    #            "--to", "notebook", "--execute",
#    #            "--ExecutePreprocessor.timeout=120",
#    #            "--ExecutePreprocessor.kernel_name=python3",
#    #            #"--output", fout.name , path]
#    #            #"--output", os.getcwd() + "/temp110518" , path]
#    #            "--output", os.getcwd() , path]
#    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
#        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
#                "--ExecutePreprocessor.timeout=120",
#                "--output", fout.name, path]
#        # submodule allows you to spawn new processes, connect to their input/
#        # output/error pipes, and obtain their return codes.
#        # print(" ".join(args))
#        subprocess.check_call(args)
#        # seek() sets the file's current position.
#        fout.seek(0)
#        nb = nbformat.read(os.getcwd() + "/temp031420.ipynb", nbformat.current_nbformat)
#        #nb = nbformat.read(fout.name, nbformat.current_nbformat)

#    #errors = [output for cell in nb.cells if "outputs" in cell
#    #            for output in cell["outputs"]\
#    #            if output.output_type == "AssertionError"]

#    stream_type = [output for cell in nb.cells if "outputs" in cell
#                for output in cell["outputs"]\
#                if output.output_type == "stream"]

#    errors = 0
#    for i in stream_type:
#        make_str = str(i)
#        # use doctest for unique string or set string message with unittest
#        if '***Test Failed***' in make_str: 
#            errors = 1
#            # print(i)

#    return nb, errors

#def test():
#    cwd = os.getcwd()
#    print(cwd)
#    # local
#    # export PYTHONPATH=${PYTHONPATH}:/home/travis/build/B612-Asteroid-Institute/adam_home
#    # notebook_path = cwd + '/PublicAppVeyor/tests/example.ipynb'
#    #notebook_path = cwd + '/tests/single_run_demo.ipynb'
#    # appveyor
#    notebook_path = cwd + '/tests/example.ipynb'
#    #_exec_notebook(notebook_path)
#    nb, errors = _process_notebook(notebook_path)

#    # assert that errors is empty, otherwise fail
#    # assert errors == []
#    # assert that errors is 0, otherwise fail
#    assert errors == 0, 'Executed Notebook Returned with ERRORS'

#def main():
#    test()


#if __name__ == "__main__":
#    main()