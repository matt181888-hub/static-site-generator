from extract_title import *
import os


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    html_nodes = markdown_to_html_node(markdown_content)
    html_string = html_nodes.to_html()
    title = extract_title(markdown_content)
    new_template = template_content.replace("{{ Title }}", title)
    newer_template = new_template.replace("{{ Content }}", html_string)
    newer_newer_template = newer_template.replace('href="/', f'href="{basepath}')
    newest_template = newer_newer_template.replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)

    os.makedirs(directory, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(newest_template)
    

    

