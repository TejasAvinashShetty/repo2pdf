from os import mkdir, chdir
from os.path import isfile, isdir
from subprocess import Popen,  PIPE


'''

Ensures a unique 'pdf' directory is ready.
First need to check that 'pdf' directory does not already exist.
Then will make one if it does not exist. Otherwise, will do nothing.
Need to report sucess to user and rest of the program. If fail raise
Folder not found error.
    '''
try:
    # We assume that we are in the folder,
    # where the git repos are stored.
    chdir('../')  # Climb to the upper directory
    if isdir('pdf') and not isfile('pdf'):
        # do nothing
        print('pdf directory exists already.')
    else:
        mkdir('pdf')
        print('pdf directory does not already exist.')
except FileNotFoundError as e: # noqa
    raise FileNotFoundError
else:
    pass
finally:
    pass


def folder_creator(repo_folder_levelled_dict):
    '''Makes the folder and builds internal structure
    Makes the folder. Also, uses the sub-folder  information
    to build the entire internal structure.
    Assumes we are inside the folder consisting the git
    cloned repository.
    Inputs:

    repo_folder_levelled_dict : dictionary
                                dictionary containing the
                                structure of the repository at
                                level. Keys are levels and values
                                are the paths to the sub-folders
                                (not files) at each level.

    Outputs:
    None
    '''
    chdir('../')
    chdir('pdf')
    for i in repo_folder_levelled_dict.keys():
        for folder in repo_folder_levelled_dict[i]:
            mkdir(folder)

    return None


def wkhtmltopdf(url, pdf_path):
    '''Interface to wkhtmltopdf
    It takes the url and the pdf_path. Then, it passes it on to
    wkhtmltopdf which then downloads and saves the pdf to the specified
    location.
    Inputs :
    url : str
          URL of the place on the internet from which we must access the
          file.

    pdf_path : str
               Path relative to the current directory where one must
               store (save) the file.

    Output:
    None
    '''
    # process = Popen(["wkhtmltopdf",
    # "https://github.com/TejasAvinashShetty/PH413/blob/master/k_cnot.py",
    # "k_cnot.pdf"])
    process = Popen(["wkhtmltopdf", url, pdf_path])
    # process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
    # (output, err) = process.communicate()

    return None
