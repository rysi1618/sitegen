import os
import shutil
from generate_html import *

orig_dir = "./static"
new_dir = "./public"
content_dir = "./content"
template_file = "./template.html"

def main():
    print(f"Removing old {new_dir}")
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    print(f"Copying files from {orig_dir} to {new_dir}")
    copy_dir_recursive(orig_dir, new_dir)
    content_file = os.path.join(content_dir, "index.md")
    html_file = os.path.join(new_dir, "index.html")
    generate_page(content_file, template_file, html_file)
    
    return 0

        

if __name__ == "__main__":
    main()