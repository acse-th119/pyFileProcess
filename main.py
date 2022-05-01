import os
import shutil


file_end = '.mkv'
new_folder = '.'
for rt, fd,fi in os.walk('.'):
    for i in fi:
        if i.endswith(file_end):
            shutil.move((os.path.join(rt,i)),new_folder)
