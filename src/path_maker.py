from os import listdir, getcwd
from os.path import isfile, isdir, join


def folder_opener(folder):
    '''Takes a folder, lists the files and subfolders
    It takes a folder supplied by the user. Then it applies
    listdir (from os module) to get a list of the contents of the
    folder. It then uses isfile and isdir (both from os.path) to sort
    the contents (as obtained above from listdir) to make 2 lists :
    one of files and other one of subfolders.

    Inputs:
    folder : string
             Path to the folder from current working directory

    Outputs:
    list_of_files_in_the_folder: list of strings
                                 list containing the strings
                                 representing the paths
                                 of the files in the folder

    list_of_sub_folders_in_the_folder: list of strings
                                       list containing the strings
                                       representing the paths
                                       of the sub-folders in the folder

    '''
    folder_contents = listdir(folder)
    list_of_files_in_the_folder = []
    list_of_sub_folders_in_the_folder = []

    for folder_member in folder_contents:
        folder_member_path = join(folder, folder_member)
        if isfile(folder_member_path) and not isdir(folder_member_path):
            list_of_files_in_the_folder.append(folder_member_path)

        elif isdir(folder_member_path) and not isfile(folder_member_path):
            list_of_sub_folders_in_the_folder.append(folder_member_path)
        else:
            raise ValueError

    return [list_of_files_in_the_folder,
            list_of_sub_folders_in_the_folder,
            folder_contents]


def path_maker(repository_name):
    '''Makes a list of the path to each repository file
    repository_member : constituents of the repository at all
                        levels subfolders, files,
                        files of subfolders and so on


    Input:

    repository_name : str
                      Name of the repository as a string or
                      Path to the repo from current working directory

    Output:
    repository_member_path_list : list of strings
                                  list containing the paths to all
                                  the files (not subfolders) of
                                  the repository.
                                  (files paths are specified
                                  with repect to the head of the
                                  repository)

    repo_folder_levelled_dict : dictionary
                                      dictionary containing the
                                      structure of the repository at
                                      level. Keys are levels and values
                                      are the paths to the sub-folders
                                      (not files) at each level.
    '''
    print('Current working directory')
    print(getcwd())
    repository_member_path_list = []
    # repo_folder_levelled_dict = {0: ['.'], }
    # repository_levelled_dict = {0: ['.'], }
    repo_folder_levelled_dict = {0: [repository_name], }
    repository_levelled_dict = {0: [repository_name], }
    i = 0

    while True:
        folder_list = repo_folder_levelled_dict[i]
        repo_folder_levelled_dict[i + 1] = []
        repository_levelled_dict[i + 1] = []
        for folder in folder_list:
            classified_contents = folder_opener(folder)
            repository_member_path_list.extend(classified_contents[0])
            repo_folder_levelled_dict[i + 1].extend(classified_contents[1])
            repository_levelled_dict[i + 1].extend(classified_contents[2])

        if repo_folder_levelled_dict[i + 1]:
            i = i + 1
            continue  # i_did_not_open_every_folder
        else:
            break  # If it is empty stop the process
            # since there are no folders

    return [repository_member_path_list,
            repo_folder_levelled_dict,
            repository_levelled_dict]
