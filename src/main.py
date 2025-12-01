from textnode import *
from copy_paste import *
from generate_page import *
from generate_pages_recursive import *
def main():
    copy_paste_wrapper("/home/matthew/static-site-generator/static", "/home/matthew/static-site-generator/public")
    generate_pages_recursive("/home/matthew/static-site-generator/content", "/home/matthew/static-site-generator/template.html", "/home/matthew/static-site-generator/public")

if __name__ == "__main__":
    main()