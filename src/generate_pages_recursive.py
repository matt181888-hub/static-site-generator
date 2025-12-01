from generate_page import *
import os
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")
    all_files = os.listdir(dir_path_content)
    for file in all_files:
        from_path = os.path.join(dir_path_content, file)
        if os.path.isfile(from_path):
            html_file = Path(file).with_suffix('.html')
            with open(from_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
            
            with open(template_path, 'r', encoding='utf-8') as file:
                template_content = file.read()
            
            html_nodes = markdown_to_html_node(markdown_content)
            html_string = html_nodes.to_html()
            title = extract_title(markdown_content)
            new_template = template_content.replace("{{ Title }}", title)
            newer_template = new_template.replace("{{ Content }}", html_string)

            final_dir = os.path.join(dest_dir_path, str(html_file))
            to_be_written_to = os.path.dirname(final_dir)
            os.makedirs(to_be_written_to, exist_ok=True)
            
            with open(final_dir, 'w') as file:
                file.write(newer_template)
        elif os.path.isdir(from_path):
            place = os.path.join(dest_dir_path, file)
            generate_pages_recursive(from_path, template_path, place)
    