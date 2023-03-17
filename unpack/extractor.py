#!/usr/bin/python
import os, zipfile, pyunpack, sys
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory

cwd = os.getcwd()
root = tk.Tk()
root.withdraw()
desktop ='C:/Somehardcoded unrar folder not in used per default'
target='C:/somehardcoded unrar target folder not used per default'

#basis_folder = file
rar_files_folder = askdirectory(title='Select Folder')
output_folder = askdirectory(title='Select Folder')


for subdir, dirs, files in os.walk(rar_files_folder):
    for file in files:
        for root, dirs, files in os.walk(rar_files_folder):
            for filename in files:
                if filename.endswith(".rar"):
                    print('Found rar files in:' + os.path.join(root, filename))
                elif filename.endswith(".zip"):
                    print('ZIP:' + os.path.join(root, filename))
                name = os.path.splitext(os.path.basename(filename))[0]
                if filename.endswith(".rar") or filename.endswith(".zip"):
                    try:
                        arch = pyunpack.Archive(os.path.join(root, filename))
                        # os.mkdir(name)
                        arch.extractall(directory=output_folder)
                    except Exception as e:
                        print("ERROR: BAD ARCHIVE " + os.path.join(root, filename))
                        print(e)
                        try:
                            # os.path.join(root,filename)os.remove(filename)
                            pass
                        except OSError as e:  # this would be "except OSError, e:" before Python 2.6
                            if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
                                raise  # re-raise exception if a different error occured
                            sys.exit()
        os._exit(0)