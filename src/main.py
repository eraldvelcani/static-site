from textnode import TextNode, TextType
from static_to_public import static_to_public
from generate_page import *
import os
import shutil
import sys


def main():
    '''node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)'''
   
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    static_to_public("/home/erald/static-site/static", "/home/erald/static-site/docs")
    
    if os.path.exists("./docs"):
        print('Deleting public dir...')
        shutil.rmtree("./docs")
    
    print("Copying static files to public dir...")
    copy_files_recursive("./static", "./docs")

    print("Generating content...")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

    
main()

