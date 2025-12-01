from textnode import *
from copy_paste import *
from generate_page import *
from generate_pages_recursive import *
from sys import *
import sys

default_basepath = "/"

def main():
    basepath = default_basepath
    print("Deleting public directory...")
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Copying static files to public directory...")
    copy_paste_wrapper("./static", "./docs")
    print("Generating content...")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)
if __name__ == "__main__":
    main()