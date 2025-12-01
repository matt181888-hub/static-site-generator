import os
import shutil

def copy_paste(source, destination):
    for name in os.listdir(source):
        src_path = os.path.join(source, name)
        dst_path = os.path.join(destination, name)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            os.mkdir(dst_path)
            copy_paste(src_path, dst_path)

def copy_paste_wrapper(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.mkdir(destination)
        copy_paste(source, destination)
    else:
        os.mkdir(destination)
        copy_paste(source, destination)



