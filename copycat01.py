#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/') # sets directory that script starts in
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_nework.txt.copy') # copies a single file
shutil.copytree('5g_research/', '5g_research_backup/') # copies a directory recursively
