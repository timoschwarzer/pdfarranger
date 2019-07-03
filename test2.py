#! /usr/bin/env python

from dogtail.utils import run
from dogtail.tree import *
from dogtail import rawinput

#os.environ['LANG']='C'
os.environ['LC_MESSAGES']='C'
#os.environ['GTK_DEBUG']='interactive'
run("python3 -m pdfarranger", appName='__main__.py')
app=root.application("__main__.py")
filemenu = app.menu('File')
filemenu.click()
filemenu.menuItem('Add').click()
filechooser = app.child(roleName='file chooser')
treeview = filechooser.child(roleName='table', name='Files')
treeview.keyCombo('<ctrl>L')
treeview.typeText('/home/robert/hmat.pdf')
filechooser.button('Open').click()
