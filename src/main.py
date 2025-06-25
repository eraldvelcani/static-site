from textnode import TextNode, TextType
from static_to_public import static_to_public
from generate_page import *
import os
import shutil


def main():
    '''node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)'''
    
    static_to_public("/home/erald/static-site/static", "/home/erald/static-site/public")
    
    if os.path.exists("./public"):
        print('Deleting public dir...')
        shutil.rmtree("./public")
    
    print("Copying static files to public dir...")
    copy_files_recursive("./static", "./public")

    print("Generating content...")
    generate_pages_recursive("./content", "./template.html", "./public")

main()

