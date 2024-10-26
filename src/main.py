import os
import shutil

from copy_static import copy_files


def main():
    root = os.getcwd()
    static = f"{root}/static"
    public = f"{root}/public"

    print("Deleting public directory...")
    if os.path.exists(public):
        shutil.rmtree(public)

    print("Copying static files to public directory...")
    copy_files(static, public)


if __name__ == "__main__":
    main()
