from markdown_to_html import *
from os import path, listdir, mkdir
from shutil import *

def main():
    rmtree("./public")
    copy_all_contents_to_new_directory("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not path.exists(dest_dir_path):
        print(f"Create destination folder for content: {dest_dir_path}")
        mkdir(dest_dir_path)

    contents = listdir(dir_path_content)

    for item in contents:
        item_path = path.join(dir_path_content, item)
        if path.isfile(item_path):
            if item.endswith(".md"):
                generate_page(item_path, template_path, dest_dir_path)
        else:
            new_dest_path = path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Creating page from {from_path} to {dest_path}, using {template_path}")
    
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page = template.replace("{{ Content }}", html)
    page = page.replace("{{ Title }}", title)

    file_name = from_path.split("/")[-1].split(".")[0]
    with open(path.join(dest_path, f"{file_name}.html"), "w") as file:
        file.write(page)
    
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

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ")

    raise Exception("Did not find h1 header")

main()