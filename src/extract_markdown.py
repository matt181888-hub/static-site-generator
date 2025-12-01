import re

def extract_markdown_images(text):
    extracted_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_images

def extract_markdown_links(text):
    extracted_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_links
