# from os import chdir, getcwd, mkdir
from path_maker import path_maker


sch_path = path_maker('test-folders/schedule')
print(sch_path[0])
print()
print(sch_path[1])
print()
print(sch_path[2])
print()
'''
[repository_member_path_list,
            repo_folder_levelled_dict,
            repository_levelled_dict] =


from path_maker import path_maker
from os import chdir, getcwd
chdir('../tests/test-folder')
s_path = path_maker(schedule)
print(s_path[0])
print()
print(s_path[1])
print()
print(s_path[2])
print()


chdir('../src')
print(getcwd())
from path_maker import path_maker
chdir('../tests')
print(getcwd())
'''
