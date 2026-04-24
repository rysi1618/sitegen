import os
import sys
import shutil
from generate_html import *

orig_dir = "./static"
new_dir = "./docs"
content_dir = "./content"
template_file = "./template.html"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print(f"Removing old {new_dir}")
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    print(f"Copying files from {orig_dir} to {new_dir}")
    copy_dir_recursive(orig_dir, new_dir)
    generate_pages_recursive(content_dir, template_file, new_dir, basepath)
    return 0

        

if __name__ == "__main__":
    main()