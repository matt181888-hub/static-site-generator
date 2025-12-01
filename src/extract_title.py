from markdown_to_html_node import *

def extract_title(markdown):
    checkem = markdown.split("\n")
    for line in checkem:
        if line[:2] == "# ":
           new_line = line.replace("#","",1)
           newer_line = new_line.strip()
           return newer_line
    raise Exception("No header")

