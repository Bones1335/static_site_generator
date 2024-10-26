import os
import shutil


def copy_files(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        to_path = os.path.join(destination, filename)
        print(f" * {from_path} => {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files(from_path, to_path)
