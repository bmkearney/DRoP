#!/usr/bin/python
#*********************************************************************************
# Super.py
# Feb. 26, 2012
# Bradley Kearney
# Superimposes protein structures that have been preprocessed by DRoP.
#*********************************************************************************

import sys
import time
import webbrowser
import os
import urllib
import shutil

def run():
    argv = sys.argv[1:]
    try:
        id=argv[0]
    except:
        return

    root =  'Renumbered/'
    if(root[-1:] != '/'):
        root += '/'
    url = '''REDACTED''''php?job=%d&status=300'%int(id)
    print url
    raw_return=urllib.urlopen(url).read()
    pdb_filenames = []
    filenames = os.listdir(os.getcwd())
    for f in filenames:
        if(f[-4:] == '.pdb'):
    	    os.rename(f, f.replace(" ", "-"))
    filenames = os.listdir(os.getcwd())
    for f in filenames:
        if(f[-4:] == '.pdb'):
            pdb_filenames.append(f)
    basis=pdb_filenames[1]
    shutil.copyfile(basis,'../Final/'+basis)
    if len(pdb_filenames)<2:
        url=''''REDACTED''''.php?job=%d&staus=333'%int(id)
        return
    for f in pdb_filenames:
        if (f!=basis):
	    os.system("python cealign.py %s %s"%(basis,f))
	    
    url = ''''REDACTED''''.php?job=%d&status=399'%int(id)
    raw_return=urllib.urlopen(url).read()
    os.chdir('../Final')
    os.system("python DRoP.py "+id)
    return
if(__name__ == '__main__'):
    run()
        
        
