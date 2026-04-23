import os
import shutil
from block_markdown import markdown_to_html_node

def copy_dir_recursive(orig_path, new_path):
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    for item in os.listdir(orig_path):
        orig_item = os.path.join(orig_path, item)
        new_item = os.path.join(new_path, item)
        print(f"--  {orig_item} -> {new_item}")
        if os.path.isfile(orig_item):
            shutil.copy(orig_item, new_item)
        else:
            copy_dir_recursive(orig_item, new_item)
        
def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No header in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = ""
    with open(from_path, 'r') as f:
        from_file = f.read()
    template_file = ""
    with open(template_path, 'r') as f:
        template_file = f.read()

    title = extract_title(from_file)
    content = markdown_to_html_node(from_file).to_html()
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", content)
    
    dest_dir = os.path.dirname(dest_path)
    if not dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_file)
    
    print(f"{dest_path} has been generated and written\n")
    
