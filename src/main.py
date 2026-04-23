import os
import shutil

orig_dir = "./static"
new_dir = "./public"

def main():
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    copy_dir_recursive(orig_dir, new_dir)
    
    return 0

def copy_dir_recursive(orig_path, new_path):
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    for item in os.listdir(orig_path):
        orig_item = os.path.join(orig_path, item)
        new_item = os.path.join(new_path, item)
        if os.path.isfile(orig_item):
            shutil.copy(orig_item, new_item)
        else:
            copy_dir_recursive(orig_item, new_item)
        
        

if __name__ == "__main__":
    main()