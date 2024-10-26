import os
import shutil

from copy_static import copy_files
from generate_page import generate_page


def main():
    root = os.getcwd()
    static = f"{root}/static"
    public = f"{root}/public"
    content = f"{root}/content"

    print("Deleting public directory...")
    if os.path.exists(public):
        shutil.rmtree(public)

    print("Copying static files to public directory...")
    copy_files(static, public)
    generate_page(content, f"{root}/template.html", public)


if __name__ == "__main__":
    main()
