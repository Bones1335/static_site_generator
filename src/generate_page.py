import os

from block_level_markdown import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {to_path} using {template_path}")

    template = open(template_path, 'r')
    template_file = template.read()
    template.close()

    for filename in os.listdir(from_path):
        markdown = open(os.path.join(from_path, filename), 'r')
        md_contents = markdown.read()
        markdown.close()

        title = extract_title(md_contents)
        html_nodes = markdown_to_html_node(md_contents)
        html_string = html_nodes.to_html()
        
        template_title = template_file.replace("{{ Title }}", title)
        template_content = template_title.replace("{{ Content }}", html_string)

        with open(f"{to_path}/index.html", "w", encoding="utf-8") as f:
            f.write(template_content)
        
