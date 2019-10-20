'''
Basically folder names don't end in a file extension.
So one can sort out folders from files.
After git cloning the repository will be present locally.
It will consist of files and folders in the first level.
After this level one will have to recursively go through each folder,
and copy the paths
'''
'''
tejas@g3:~/git-tejas/repo2pdf/tests/test-folders/schedule/
schedule-master$ python
Python 2.7.15+ (default, Oct  7 2019, 17:39:04)
[GCC 7.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>>
>>> for root, dirs, files in os.walk("."):
...     for filename in files:
...         print(filename)
...
test_schedule.py
setup.py
MANIFEST.in
requirements-dev.txt
HISTORY.rst
LICENSE.txt
README.rst
FAQ.rst
.gitignore
.travis.yml
AUTHORS.rst
tox.ini
faq.rst
api.rst
index.rst
Makefile
conf.py
placeholder.txt
sidebarintro.html
__init__.py
>>> root
'./schedule'
>>> dirs
[]
>>> os.listdir(".")
['test_schedule.py', 'setup.py', 'MANIFEST.in', 'requirements-dev.txt',
'HISTORY.rst', 'LICENSE.txt', 'docs', 'README.rst', 'FAQ.rst',
'schedule', '.gitignore', '.travis.yml', 'AUTHORS.rst', 'tox.ini']
>>> os.listdir("/schedule")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 2] No such file or directory: '/schedule'
>>> os.listdir("schedule")
['__init__.py']
>>> os.listdir("docs")
['faq.rst', '_static', 'api.rst', 'index.rst', 'Makefile', 'conf.py',
'_templates']
>>> import glob
>>> print(glob.glob("./*"))
['./test_schedule.py', './setup.py', './MANIFEST.in',
'./requirements-dev.txt', './HISTORY.rst', './LICENSE.txt', './docs',
'./README.rst', './FAQ.rst', './schedule', './AUTHORS.rst', './tox.ini']
>>> import os
>>>
>>> def get_filepaths(directory):
...     """
...     This function will generate the file names in a directory
...     tree by walking the tree either top-down or bottom-up.
        For each
...     directory in the tree rooted at directory top (including top
        itself),
...     it yields a 3-tuple (dirpath, dirnames, filenames).
...     """
...     file_paths = []  # List which will store all of the full
        filepaths.
...
>>>     # Walk the tree.
...     for root, directories, files in os.walk(directory):
  File "<stdin>", line 2
    for root, directories, files in os.walk(directory):
    ^
IndentationError: unexpected indent
>>>         for filename in files:
  File "<stdin>", line 1
    for filename in files:
    ^
IndentationError: unexpected indent
>>>             # Join the two strings in order to form the full
                  filepath.
...             filepath = os.path.join(root, filename)
  File "<stdin>", line 2
    filepath = os.path.join(root, filename)
    ^
IndentationError: unexpected indent
>>>             file_paths.append(filepath)  # Add it to the list.
  File "<stdin>", line 1
    file_paths.append(filepath)  # Add it to the list.
    ^
IndentationError: unexpected indent
>>>
>>>     return file_paths  # Self-explanatory.
  File "<stdin>", line 1
    return file_paths  # Self-explanatory.
    ^
IndentationError: unexpected indent
>>>
>>> # Run the above function and store its results in a vari
...
>>> def files(path):
...     for file in os.listdir(path):
...         if os.path.isfile(os.path.join(path, file)):
...             yield file
...
>>> for file in files("."):
...     print (file)
...
test_schedule.py
setup.py
MANIFEST.in
requirements-dev.txt
HISTORY.rst
LICENSE.txt
README.rst
FAQ.rst
.gitignore
.travis.yml
AUTHORS.rst
tox.ini
>>>

'''
