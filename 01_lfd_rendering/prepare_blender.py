#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
from subprocess import call

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))
from global_variables import *

if not os.path.exists(g_3rd_party_folder):
    os.mkdir(g_3rd_party_folder) 

# download and unzip blender
filename = os.path.join(g_3rd_party_folder, 'blender.tar.bz2')
call(['wget', '-O', filename, g_blender_executable_url])
blender_folder = os.path.dirname(g_blender_executable_path)
if not os.path.exists(blender_folder):
    os.mkdir(blender_folder) 
call(['tar', 'xvjf', filename, '-C', blender_folder, '--strip-components=1'])
os.remove(filename)