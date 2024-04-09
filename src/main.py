from markdown_to_html import *
from os import *
from shutil import *

def main():
    rmtree("../public")
    copy_all_contents_to_new_directory("../static", "../public")

    
def copy_all_contents_to_new_directory(source_path, dest_path):

    print(f"Copying files to {dest_path}")

    if not path.exists(source_path):
        raise Exception("Source path does not exist")
    
    if not path.exists(dest_path):
        print(f"Create destination folder: {dest_path}")
        mkdir(dest_path)

    contents = listdir(source_path)

    for item in contents:
        item_path = path.join(source_path, item)
        if path.isfile(item_path):
            print(f"Copy file: {item_path}")
            copy(item_path, dest_path)
        else:
            new_dest_path = path.join(dest_path, item)
            copy_all_contents_to_new_directory(item_path, new_dest_path)


main()