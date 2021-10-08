#!/usr/bin/env python3

import glob
import os
import shutil
import pathlib
from os.path import expanduser
home = expanduser("~")

file_path = None

for (root,dirs,files) in os.walk('.pio', topdown=True):
    if "firmware.bin" in files:
        # print(root)
        # print(dirs)
        # print(files)
        file_path = os.path.join(root, "firmware.bin")
        print(file_path)
        print('--------------------------------')

if file_path:
    shutil.copyfile(file_path, pathlib.Path(f"{home}/{os.path.basename(file_path)}"))