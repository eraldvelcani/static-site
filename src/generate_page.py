import os
from blocks import *
from pathlib import Path
import shutil

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('#'):
            return line.strip()
    raise Exception

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, 'r')
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, 'r')
    template_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace('href="/', 'href="{basepath}')
    template_content = template_content.replace('href="/', 'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != '':
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, 'w')
    to_file.write(template_content)
    to_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

