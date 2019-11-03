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
except FileNotFoundError as e:
    raise FileNotFoundError
else:
    pass
finally:
    pass


