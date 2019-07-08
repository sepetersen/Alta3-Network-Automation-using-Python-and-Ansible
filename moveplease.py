#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/') # script runs in this directory

shutil.move('raynor.obj', 'ceph_storage/') # move file to ceph_storage directory

xname = input ('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
    # rename based on input
