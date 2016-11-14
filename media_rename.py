#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

assert sys.version_info >= (3,0)

#-------------------------------------------------------------------------------
# CHOOSE TO READ OR WRITE
#-------------------------------------------------------------------------------
'''
def process():
    print ( "Do you want to generate a list or rename the files?")
    choice = input("[Y/n]: ")
    if choice.lower() == "y":
        newname()
    elif choice.lower() == "n" or choice.lower() == "":
        getfile()
    '''
# -------------------------------------------------------------------------------
# GENERATE LIST
# -------------------------------------------------------------------------------
def getfile():
    cwd = os.getcwd()

    # get a list of files that have the extension txt
    filelist = filter(lambda f: f.split('.')[-1] == 'txt', os.listdir(cwd))
    filelist = sorted(filelist)
    read( filelist[0])

'''
def newname():
    cwd = os.getcwd()

    # get a list of files that have the extension mkv
    filelist = filter(lambda f: f.split('.')[-1] == 'mkv', os.listdir(cwd))
    filelist = sorted(filelist)

    namelist = {}
    # list each file
    for file in filelist:
        newname = input( file + ": ")
        namelist.setdefault( file, newname)

    save_obj(namelist, "realtitles")
'''
#-------------------------------------------------------------------------------
# SAVE OR LOAD CONFIG
#-------------------------------------------------------------------------------
# saves list


def read( file):
    txt = open(file, 'r').read()

    for f in txt.split("\n"):
        try:
            if sys.version_info <= (2,9):
                f = f.decode('string_escape')
            rename(f)
        except:
            print ('Error:', oldTitle)

'''
#OLD RENAME
def rename():
    namelist = load_obj( "realtitles")
    for k, v in namelist.items():
        os.rename(k, v + k[-4:])
'''

def rename(title):
    oldTitle, newTitle = title.split( ' = ')
    newTitle = newTitle.replace(':', ' -')

    plexExtras = {'behindthescenes': 'Behind The Scenes',
                 'deleted': 'Deleted Scenes',
                 'featurette': 'Featurettes',
                 'interview': 'Interviews',
                 'scene': 'Scenes',
                 'short': 'Shorts',
                 'trailer': 'Trailers'
                 }
    print( newTitle)

    if ' | ' in newTitle:
        newTitle, subfolder = newTitle.split(' | ')
        if subfolder in plexExtras:
            if os.path.exists( plexExtras[ subfolder]) == False:
                os.mkdir( plexExtras[ subfolder])

            path = plexExtras[ subfolder] + '/' + newTitle + oldTitle[-4:]
            os.rename(oldTitle, path)
            print("Rename:", oldTitle, plexExtras[ subfolder] + '/' + newTitle + oldTitle[-4:])
        else:
            os.rename( oldTitle, newTitle + oldTitle[-4:])
    else:
        os.rename(oldTitle, newTitle + oldTitle[-4:])


if __name__ == "__main__":
    #process()
    getfile()