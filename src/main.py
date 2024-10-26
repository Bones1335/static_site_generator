import os
import shutil

from copy_static import copy_files
from generate_page import generate_pages


def main():
    root = os.getcwd()
    static = f"{root}/static"
    public = f"{root}/public"
    content = f"{root}/content"
    template = f"{root}/template.html"

    print("Deleting public directory...")
    if os.path.exists(public):
        shutil.rmtree(public)

    print("Copying static files to public directory...")
    copy_files(static, public)

    print("Generating page...")
    generate_pages(content, template, public)


if __name__ == "__main__":
    main()
