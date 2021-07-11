from genericpath import isfile
import os
import os.path
import shutil
from pathlib import Path

path = os.getcwd()

def home_directory():
    print('1. Directories')
    print('2. Files')
    print('3. Close the directory')

def in_directories():
    print('1. Rename Directory')
    print('2. Number of files')
    print('3. Number of directories')
    print('4. Content of the directory')
    print('5. Add file to this directory')
    print('6. Add new directory to this directory')

def in_files():
    print('1. Delete file')
    print('2. Rename file')
    print('3. Add content to this file')
    print('4. Rewrite content of this file')
    print('5. Return to the parent directory')

def rename_dir():
    try: 
        current = input('Enter name of the directory: ')
        new = input('Enter the name to rename: ')
        os.rename(current, new)
    except FileNotFoundError:
        print('File not found!!!')

def quan_of_files_dir():
    cnt = 0
    with os.scandir(path) as file:
        for i in file:
            if i.is_file():
                cnt+=1
    print('Number of files in this directory = {}'.format(cnt))

def quan_of_dir():
    cnt = 0
    with os.scandir(path) as dir:
        for i in dir:
            if i.is_dir():
                cnt+=1
    print('Number of directories in this directory = {}'.format(cnt))

def content_dir():
    cont = os.listdir('dir')
    for i in cont:
        print(i)

def add_file_dir():
    name = input('Enter the name to create new file:')
    if name.isfile():
        name = input('File with this name already exist. Enter another name:')
    with open(name, 'x') as f:
        print('File successfully created')
    

def add_dir_dir():
    name = input('Enter the name to create new directory:')
    if name.isdir():
        name = input('Directory with this name already exist. Enter another name:')
    os.mkdir(name)
    print('Directory successfully created')

def delete_file():
    try:
        name = input('Enter the name of file to delete:')
        os.remove(name)
        print('File deleted')
    except FileNotFoundError:
        print("You incorrectly wrote it OR this file does not exist")
    
def rename_file():
    try: 
        current = input('Enter the file name which you want to rename:')
        new = input('Enter the new name of the file:')
        os.rename(current, new)
    except FileNotFoundError:
        print("You incorrectly wrote it OR this file does not exist")

def add_cont_file():
    try:
        name = input('Name of the file where you want to add content:')
        with open(name, 'a') as f:
            f.write(input())
        print('Content successfully added')
    except FileNotFoundError:
        print("You incorrectly wrote it OR this file does not exist")

def rewrite_file():
    try:
        name = input('Name of the file where you want to rewrite content:')
        with open(name, 'w') as f:
            f.write(input())
        print('Content successfully added')
    except FileNotFoundError:
        print("You incorrectly wrote it OR this file does not exist")

def return_file():
    try:
        file = input('Enter full path:')
        path = Path(file).parent
        print(path)
    except FileNotFoundError:
        print('File not found!!!')

while(True):
    current_place = os.getcwd()
    home_directory()
    print(f'Current directory is: {current_place}')
    in_where = int(input('Choose the number:'))

    if in_where == 1:
        in_directories()
        option = int(input('Options. Choose the number:' ))
        if option == 1:
            rename_dir()
        if option == 2:
            quan_of_files_dir()
        if option == 3:
            quan_of_dir()
        if option == 4:
            content_dir()
        if option == 5:
            add_file_dir()
        if option == 6:
            add_dir_dir()
        else:
            continue
    if in_where == 2:
        in_files()
        option = int(input('Options. Choose the number:' ))
        if option == 1:
            delete_file()
        if option == 2:
            rename_file()
        if option == 3:
            add_cont_file()
        if option == 4:
            rewrite_file()
        if option == 5:
            return_file()
        else:
            continue
        
    if in_where == 3:
        print('OK')
        break
    else:
        continue