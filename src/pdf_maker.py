from os import mkdir, chdir
from os.path import isfile, isdir


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
    chdir('pdf')
    for i in repo_folder_levelled_dict.keys():
        for folder in repo_folder_levelled_dict[i]:
            mkdir(folder)

    return None
